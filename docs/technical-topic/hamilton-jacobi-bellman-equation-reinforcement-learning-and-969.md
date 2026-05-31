---
id: 969
url: https://dani2442.github.io/posts/continuous-rl/
title: 'Hamilton-Jacobi-Bellman Equation: Reinforcement Learning and Diffusion Models
  | dani2442''s Blog'
domain: dani2442.github.io
source_date: '2026-03-30'
tags:
- ai
- academic-paper
- llm
summary: The blog post explores the mathematical foundations connecting the Hamilton-Jacobi-Bellman
  (HJB) equation—a principle from optimal control theory dating back to Richard Bellman's
  1952 work on dynamic programming—to modern applications in continuous-time reinforcement
  learning and diffusion models. The author derives the HJB equation for both deterministic
  and stochastic controlled systems, showing how it generalizes the discrete-time
  Bellman equation to continuous settings with noise, and demonstrates how this framework
  naturally unifies several machine learning topics including stochastic optimal control
  and generative model training. The post emphasizes that this classical mathematical
  structure provides a principled foundation for understanding and solving modern
  reinforcement learning problems through policy iteration and other optimization
  techniques.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Hamilton-Jacobi-Bellman Equation: Reinforcement Learning and Diffusion Models | dani2442's Blog

Table of Contents

![](/posts/continuous-rl/continuous_rl.drawio.svg)

Machine learning feels recent, but one of its core mathematical ideas dates back to 1952, when Richard Bellman published a seminal paper titled “On the Theory of Dynamic Programming” [[6, 7]](#references), laying the foundation for optimal control and what we now call reinforcement learning.

Later in the 50s, Bellman extended his work to continuous-time systems, turning the optimal condition into a PDE. What he later found was that this was identical to a result in physics published a century before (1840s), known as the Hamilton-Jacobi equation.

Once that structure is visible, several topics line up naturally:

* continuous-time reinforcement learning
* stochastic control
* diffusion models
* optimal transport

In this post I want to turn our attention to two applications of Bellman’s work: continuous-time reinforcement learning, and how the training of generative models (diffusion models) can be interpreted through stochastic optimal control

1. Introduction[#](#1-introduction)
-----------------------------------

Bellman originally formulated dynamic programming in discrete time in the early 1950s [[6, 7]](#references). Consider a Markov decision process with state space $\mathcal X$, action space $\mathcal A$, transition kernel $P(\cdot\mid x,a)$, reward function $r(x,a)$, and discount factor $\gamma\in(0,1)$. A policy $\pi$ maps each state to a distribution over actions. If the state evolves as a controlled Markov chain

$$
X\_{n+1}\sim P(\cdot\mid X\_n,a\_n),
$$

with one-step reward $r(x,a)$ and discount factor $\gamma\in(0,1)$, then the objective is

$$
J(\pi):=\mathbb E\left[\sum\_{n=0}^\infty \gamma^n r(X\_n,a\_n)\right],\qquad a\_n\sim \pi(\cdot\mid X\_n),
$$

and the value function is defined as:

$$
V(x):=\sup\_\pi \mathbb E\left[\sum\_{n=0}^\infty \gamma^n r(X\_n,a\_n)\,\middle|\,X\_0=x\right].
$$

Under mild conditions, $V$ satisfies the Bellman equation

$$
V(x)=\max\_{a\in\mathcal A}\left\{r(x,a)+\gamma\,\mathbb E \left[V(X\_{n+1})\mid X\_n=x,a\_n=a\right]\right\}.\tag{Bellman equation}
$$
> This says: choose the action that maximizes immediate reward plus continuation value. Continuous time keeps the same local logic, but now the time step has length $h$ and we send $h\downarrow 0$.

To isolate the main idea, first ignore noise and consider the non-autonomous deterministic control system

$$
\dot X\_s = f(s,X\_s,a\_s),\qquad X\_t=x,
$$

with finite-horizon value function

$$
V(t,x):=\sup\_{a\_\cdot}\left[\int\_t^T r(s,X\_s,a\_s)\,ds+g(X\_T)\,\middle|\,X\_t=x\right].
$$
> **Theorem (HJB, deterministic non-autonomous).** For $V\in C^1$, the value function satisfies
>
> $$
> > -\partial\_t V(t,x) = H\bigl(t,x,\nabla\_x V(t,x)\bigr), \tag{HJB}
> > $$
>
> where the **Hamiltonian** is $H(t,x,p):=\sup\_{a\in\mathcal A}\left\{r(t,x,a)+p^\top f(t,x,a)\right\}$.

*Proof.* Fix $(t,x)$ and $h>0$. The dynamic programming principle gives

$$
V(t,x)=\sup\_{a\_\cdot}\left[\int\_t^{t+h} r(s,X\_s,a\_s)\,ds + V(t+h,X\_{t+h})\right].
$$

To first order in $h$, it is enough to optimize over constant actions $a$ on $[t,t+h]$. For smooth $V$ and deterministic dynamics:

$$
V(t+h,X\_{t+h})=V(t,x)+h\,\partial\_t V(t,x)+h\,\nabla\_x V(t,x)^\top f(t,x,a)+o(h),
$$$$
\int\_t^{t+h} r(s,X\_s,a)\,ds = h\,r(t,x,a)+o(h).
$$

Substituting into the DPP, cancelling $V(t,x)$, dividing by $h$, and letting $h\downarrow 0$:

$$
0=\sup\_{a\in\mathcal A}\left\{r(t,x,a)+\nabla\_x V(t,x)^\top f(t,x,a)+\partial\_t V(t,x)\right\},
$$

which rearranges to $-\partial\_t V(t,x) = H(t,x,\nabla\_x V(t,x))$. $\quad\blacksquare$

**Connection to Hamilton–Jacobi.** What Bellman realized in the 1950s is that the partial differential equation produced by dynamic programming has exactly the same structure as the 19th-century Hamilton–Jacobi equation from classical mechanics. Writing the running reward as minus a Lagrangian, $r(t,x,a)=-L(t,x,a)$, define

$$
H(t,x,p):=\sup\_{a\in\mathcal A}\{p^\top f(t,x,a)-L(t,x,a)\}.
$$

The HJB equation then becomes identical to Hamilton’s equation for the action $S(t,q)$,

$$
\frac{\partial S}{\partial t}+H\!\left(q,\frac{\partial S}{\partial q}\right)=0.
$$

Under the correspondence $S\leftrightarrow V$ and $q\leftrightarrow x$, the two equations are the same at the level of PDE structure.

### Controlled diffusions (Itô processes)[#](#controlled-diffusions-itô-processes)

We now move to the stochastic setting: continuous time, continuous state and action spaces, and Itô dynamics. Assume the system evolves according to the SDE

$$
dX\_t = f(X\_t,a\_t)\,dt + \Sigma(X\_t,a\_t)\,dW\_t
$$

where $X\_t$ is the state, $a\_t$ is the control, $W\_t$ is a standard Wiener process, and $f$ and $\Sigma$ describe drift and diffusion. The reward is given by $r(x,a)$, and the objective is to maximize expected discounted reward over an infinite horizon:

$$
J(\pi):=\mathbb{E}\Big[\int\_0^\infty e^{-\rho t}r(X\_t,a\_t)\,dt\Big],\qquad a\_t\sim \pi(\cdot\mid X\_t)
$$

where $\rho>0$ is the discount rate. The associated value function is

$$
V(x):=\sup\_\pi \mathbb{E}\Big[\int\_0^\infty e^{-\rho t}r(X\_t,a\_t)\,dt \Big| X\_0=x\Big]
$$
> **Theorem (Hamilton-Jacobi-Bellman equation for a controlled diffusion).** Under suitable regularity conditions:
>
> 1. $f(\cdot,a)$, $\Sigma(\cdot,a)$, $r(\cdot,a)$ are continuous in $(x,a)$; Lipschitz in $x$ uniformly in $a$.
> 2. $\Sigma\Sigma^\top(x,a)$ is bounded and uniformly nondegenerate (for classical $C^2$ theory; if you drop this you typically work in viscosity form).
> 3. $r$ is bounded (or has at most linear growth with enough integrability).
> 4. $V\in C^2(\mathbb R^d)$ and bounded (or polynomial growth, with the usual technical modifications).
>
> Then the value function satisfies the *Hamilton-Jacobi-Bellman* (HJB) PDE
>
> $$ \rho V(x)=\max\_{a\in \mathcal{A}}\Big\{ r(x,a)+\mathcal{L}^a V(x)\Big\}.\tag{1} $$
>
> where $\mathcal{L}^a$ is the infinitesimal generator under action $a$:
>
> $$ \mathcal{L}^a \varphi(x):=\nabla \varphi(x)^\top f(x,a)
> +\tfrac12 \mathrm{Tr}\big(\Sigma\Sigma^\top \nabla^2 \varphi(x)\big) $$

*Proof.* The structure is the same as in the deterministic case. The only new ingredient is the short-time expansion of $\mathbb E\_x[V(X\_h)]$: by Itô’s formula,

$$
\mathbb E\_x[V(X\_h)] = V(x) + h\,\mathcal L^a V(x) + o(h),
$$

where the generator $\mathcal{L}^a$ replaces the directional derivative $\nabla V^\top f$, adding the curvature term $\tfrac{1}{2}\mathrm{Tr}(\Sigma\Sigma^\top\nabla^2 V)$ coming from the quadratic variation of $W$. The rest is unchanged: substitute into the DPP, cancel $V(x)$, divide by $h$, and let $h\downarrow 0$ to obtain (1). $\quad\blacksquare$

The same argument also yields the non-autonomous HJB when $f$, $\Sigma$, and $r$ depend explicitly on time; see [Appendix C](#appendix-c-non-autonomous-case).

> **Historical Note:** In 1960, Rudolf E. Kalman published his seminal paper on the linear-quadratic regulator (LQR) problem [[8]](#references), which is a continuous-time optimal control problem with linear dynamics and quadratic cost. The solution to the LQR problem is given by the algebraic Riccati equation, which can be derived from the Hamilton-Jacobi-Bellman (HJB) equation for continuous-time control problems.

2. Continuous-time Reinforcement Learning[#](#2-continuous-time-reinforcement-learning)
---------------------------------------------------------------------------------------

Define the continuous-time analogue of the **Q-function** by

$$
Q(x,a):=\frac{1}{\rho}\Big(r(x,a)+\mathcal{L}^a V(x)\Big).\tag{2}
$$

From the HJB (1), it follows immediately that $V(x)=\max\_{a} Q(x,a)$. This identity is the basis of **policy improvement**: once we have an estimate of $V$, the greedy action is $a^\*(x) = \arg\max\_a Q(x,a)$.

This stationary, discounted form is the RL convention used in the next two sections.

### 2.1 Policy Iteration[#](#21-policy-iteration)

We solve the HJB numerically with policy iteration (PI), alternating between *evaluating* the current policy and *improving* it through the Q-function. Both the value $V\_\theta$ and the policy $\alpha\_\phi$ are represented by MLPs.

This algorithm is **model-based**: it assumes known dynamics through $f(x,a)$ and $\Sigma(x,a)$ (equivalently, access to the generator $\mathcal L^a$). The model is used both to simulate closed-loop trajectories in policy evaluation and to compute $\mathcal L^aV$ in policy improvement.

We iterate the following steps until convergence:

1. **Policy evaluation** (value under current policy $\alpha\_k$):

   $$
   \rho V\_k(x)=r\big(x,\alpha\_k(x)\big)+\mathcal{L}^{\alpha\_k(x)}V\_k(x).
   $$

   In practice, we estimate $V\_k\approx V^{\alpha\_k}$ by Monte Carlo rollouts of the closed-loop SDE and fit $V\_\theta$ by regression.
2. **Policy improvement** (greedy with respect to $V\_k$):

   $$
   \alpha\_{k+1}(x)\in\arg\max\_{a\in\mathcal A}\{r(x,a)+\mathcal L^aV\_k(x)\}
   =\arg\max\_{a\in\mathcal A} Q\_k(x,a),
   $$

   where

   $$
   Q\_k(x,a):=\frac{1}{\rho}\big(r(x,a)+\mathcal L^aV\_k(x)\big).
   $$

   With a differentiable actor $\alpha\_\phi$, this becomes gradient ascent on

   $$
   \max\_\phi\;\mathbb E\_x\big[Q\_k\big(x,\alpha\_\phi(x)\big)\big].
   $$
3. **Diagnosis / stopping**:

   $$
   \mathcal R\_{\mathrm{HJB}}(x)=\rho V(x)-\max\_a\{r(x,a)+\mathcal L^aV(x)\},
   $$

   and stop when sampled norms of $\mathcal R\_{\mathrm{HJB}}$ and parameter changes plateau.

Intuition: evaluation estimates the value landscape induced by the current policy, and improvement moves the policy uphill on that landscape. Repeating the two steps drives $(V,\alpha)$ toward a fixed point of the HJB.

### Computing the generator $\mathcal{L}^a V$[#](#computing-the-generator)

The generator requires $\nabla V$ and $\nabla^2 V$, obtained from $V\_\theta$ via autograd. The diffusion $\Sigma(x,a)$ is problem-given (model-based setting).

```
def compute_generator(V_net, x, f_xa, Sigma_xa):
    """L^a V(x) = ∇V · f + ½ Tr(ΣΣᵀ ∇²V)."""
    V = V_net(x)                                                # (batch, 1)
    grad_V = autograd.grad(V.sum(), x, create_graph=True)[0]    # (batch, d)
    drift  = (grad_V * f_xa).sum(-1, keepdim=True)              # ∇V · f
    d = x.shape[1]
    H = torch.stack([autograd.grad(grad_V[:,i].sum(), x,
                     create_graph=True)[0] for i in range(d)], dim=1)
    A = Sigma_xa @ Sigma_xa.transpose(-1,-2)                    # ΣΣᵀ
    diff = 0.5 * (A * H).sum(dim=(-2,-1)).unsqueeze(-1)         # ½Tr(AH)
    return drift + diff
```

During policy improvement, $\nabla V$ and $\nabla^2 V$ are *detached* from $\theta$ so gradients flow only through $\phi$.

### Policy evaluation (Feynman–Kac MC)[#](#policy-evaluation-feynmankac-mc)

For a fixed policy $\alpha$, $V^\alpha$ solves the linear PDE

$$
\rho V^\alpha(x)=r\big(x,\alpha(x)\big)+\mathcal L^{\alpha(x)}V^\alpha(x).
$$

By the Feynman-Kac representation, for any truncation horizon $T>0$,

$$
V^\alpha(x)=
\mathbb E\_x\!\left[\int\_0^\infty e^{-\rho s}\,r\big(X\_s,\alpha(X\_s)\big)\,ds\right]=\mathbb E\_x\!\left[\int\_0^T e^{-\rho s}\,r\big(X\_s,\alpha(X\_s)\big)\,ds + e^{-\rho T}V^\alpha(X\_T)\right]
$$

In Monte Carlo policy evaluation, we approximate this expectation with simulated trajectories and use the critic to bootstrap the terminal value at time $T$.

### Policy improvement[#](#policy-improvement)

At collocation points, compute $Q\_k(x,\alpha\_\phi(x))$ using the detached $\nabla V\_k$, $\nabla^2 V\_k$, and maximise $\mathbb{E}[Q\_k]$ w.r.t. $\phi$:

```
grad_V, H = compute_generator_detached(V_net, x)   # frozen V
a    = policy_net(x)                                 # differentiable in φ
f_xa, S_xa = problem.drift(x, a), problem.diffusion(x, a)
L_V  = generator_from_precomputed(grad_V, H, f_xa, S_xa)
Q    = (problem.reward(x, a) + L_V) / rho
loss = -Q.mean()            # gradient ascent on Q
loss.backward()
opt_pi.step()
```

### 2.2 Model-Free: Continuous-Time Q-learning[#](#22-model-free-continuous-time-q-learning)

Policy iteration is model-based. A complementary route is **Q-learning**, which can be implemented model-free from sampled transitions.

In continuous time, the Q-function satisfies the PDE

$$
\rho Q(x,a)=r(x,a)+\mathcal L^a\big(\max\_{a'\in\mathcal A}Q(x,a')\big).\tag{4}
$$

With neural networks, set

$$
Q\_\psi(x,a)\approx Q(x,a),\qquad a\_\omega(x)\approx \arg\max\_{a}Q\_\psi(x,a),
$$

where $Q\_\psi$ (critic) and $a\_\omega$ (actor) are MLPs.

Using short transitions $(X\_t,a\_t,r\_t,X\_{t+\Delta t})$ and a small step size $\Delta t$, a practical TD target is

$$
y\_t = r\_t\,\Delta t + e^{-\rho\Delta t}\,\bar V(X\_{t+\Delta t}),
\qquad
\bar V(x):=Q\_{\bar\psi}(x,a\_\omega(x))\ \text{(or }\max\_a Q\_{\bar\psi}(x,a)\text{)}.
$$

Then train the critic with

$$
\mathcal L\_Q(\psi)=\mathbb E\big[(Q\_\psi(X\_t,a\_t)-y\_t)^2\big].
$$

The actor is updated by ascent on

$$
\max\_\omega\;\mathbb E\big[Q\_\psi(X\_t,a\_\omega(X\_t))\big].
$$

This mirrors the usual actor-critic split: one network fits state-action values, while the other outputs actions that maximize them.

### Example 1 — Stochastic LQR[#](#example-1--stochastic-lqr)

The linear-quadratic regulator is the canonical continuous-time control benchmark: linear dynamics, quadratic cost, and a closed-form solution. That makes it ideal for validating a numerical solver.

#### Problem setup[#](#problem-setup)

**Dynamics** (additive noise, 1-D scalar):

$$dX\_t = (\alpha\,X\_t + \beta\,a\_t)\,dt + \sigma\,dW\_t$$

**Reward** (negative quadratic cost):

$$r(x,a) = -\tfrac{1}{2}(q\,x^2 + r\_a\,a^2)$$

| Symbol | Meaning | Value |
| --- | --- | --- |
| $\alpha$ | open-loop drift (stable if $<0$) | $-0.5$ |
| $\beta$ | control effectiveness | $1.0$ |
| $q$ | state cost weight | $1.0$ |
| $r\_a$ | action cost weight | $0.1$ |
| $\sigma$ | diffusion (noise intensity) | $0.3$ |
| $\rho$ | discount rate | $0.1$ |

#### Analytical solution[#](#analytical-solution)

Substituting a quadratic ansatz $V(x) = -\tfrac{1}{2}Px^2 - c$ into the HJB and optimising over $a$ yields (see [Appendix A](#appendix-a-lqr-derivation) for the full derivation):

The closed-form objects are:

$$
a^\*(x)=-\frac{\beta P}{r\_a}x=: -Kx,
$$$$
\rho P = q + 2\alpha P - \frac{\beta^2}{r\_a}P^2,
$$$$
c = \frac{\sigma^2 P}{2\rho}.
$$

#### Code[#](#code)

```
class StochasticLQR(ControlProblem):
    def drift(self, x, a):     return x @ A.T + a @ B.T
    def diffusion(self, x, a): return D.unsqueeze(0).expand(x.shape[0], -1, -1)
    def reward(self, x, a):
        return -0.5*((x@Q*x).sum(-1,keepdim=True) + (a@R*a).sum(-1,keepdim=True))

P, c, K = solve_are(A, B, Q, R, D, rho=0.1)    # exact Riccati solution
solver  = PolicyIteration(problem, cfg)
history = solver.solve()                          # neural PI
```

#### Results[#](#results)

Learned $V\_\theta$ and $\alpha\_\phi$ closely match $V^\*(x) = -\tfrac{1}{2}Px^2 - c$ and $a^\*(x) = -Kx$:

![LQR — Value function and policy](/posts/continuous-rl/lqr_value_policy.png)

Sample trajectories under the learned policy ($x\_0=1.5$) and cumulative discounted reward:

![LQR — Trajectory and reward](/posts/continuous-rl/lqr_trajectory.png)

Convergence diagnostics (value-fit MSE, policy objective, HJB residual):

![LQR — Convergence](/posts/continuous-rl/lqr_convergence.png)

---

### Example 2 — Merton Portfolio[#](#example-2--merton-portfolio)

Merton’s (1969) portfolio problem asks how an investor should allocate wealth between a risk-free bond and a risky asset while also choosing a consumption rate. The objective is to maximize expected lifetime CRRA (constant relative risk aversion) utility of consumption. It also admits a closed-form solution, making it a useful second benchmark with *multiplicative* noise rather than the additive noise of LQR.

#### Problem setup[#](#problem-setup-1)

**State:** wealth $X\_t > 0$. **Controls:** $a\_t = (\pi\_t, k\_t)$ — risky-asset fraction and consumption-to-wealth ratio $k = c/X$.

**Dynamics** (geometric / multiplicative noise):

$$dX\_t = \big[r\_f + \pi\_t(\mu - r\_f) - k\_t\big] X\_t dt + \pi\_t \sigma X\_t dW\_t$$

**Reward** (CRRA utility of consumption flow, $\gamma \neq 1$):

$$r(x,a) = \frac{(k\,x)^{1-\gamma}}{1-\gamma}$$

| Symbol | Meaning | Value |
| --- | --- | --- |
| $r\_f$ | risk-free rate | $0.03$ |
| $\mu$ | risky asset expected return | $0.08$ |
| $\sigma$ | risky asset volatility | $0.20$ |
| $\gamma$ | relative risk aversion (CRRA) | $2.0$ |
| $\rho$ | subjective discount rate | $0.05$ |

#### Analytical solution[#](#analytical-solution-1)

Substituting a power-law ansatz $V(x) = \frac{A}{1-\gamma}x^{1-\gamma}$ into the HJB and optimising over $(\pi, k)$ yields (see [Appendix B](#appendix-b-merton-derivation) for the full derivation):

The closed-form controls and value are:

$$
\pi^\*=\frac{\mu-r\_f}{\gamma\sigma^2}=0.625,
$$$$
k^\*=\frac{\rho-(1-\gamma)M}{\gamma},\qquad
M:=r\_f+\frac{(\mu-r\_f)^2}{2\gamma\sigma^2},\qquad
k^\*\approx 0.0478,
$$$$
V^\*(x)=\frac{A}{1-\gamma}x^{1-\gamma},\qquad
A=\left(\frac{\gamma}{\rho-(1-\gamma)M}\right)^\gamma.
$$

Both optimal controls are *constant* — independent of wealth and time.

#### Code[#](#code-1)

```
class MertonProblem(ControlProblem):
    def drift(self, x, a):                              # a = (π, c_rate)
        pi, cr = a[:, 0:1], a[:, 1:2]
        return (self.r_f + pi*(self.mu - self.r_f) - cr) * x
    def diffusion(self, x, a):
        return (a[:, 0:1] * self.sigma * x).unsqueeze(-1)
    def reward(self, x, a):
        c = (a[:, 1:2] * x).clamp(min=1e-8)
        return c.pow(1 - self.gamma) / (1 - self.gamma)
```

#### Results[#](#results-1)

Learned value function matches the exact power-law $V^\*\propto x^{1-\gamma}$; both controls converge to the analytical constants:

![Merton — Value function and policy](/posts/continuous-rl/merton_value_policy.png)

Sample wealth trajectories under the learned policy ($X\_0 = 1$) and cumulative discounted reward:

![Merton — Trajectory and reward](/posts/continuous-rl/merton_trajectory.png)

Convergence diagnostics:

![Merton — Convergence](/posts/continuous-rl/merton_convergence.png)

3. Diffusion Models[#](#3-diffusion-models)
-------------------------------------------

The same HJB machinery also appears in diffusion models once reverse-time sampling is written as a control problem. Let $p\_{\text{data}}(x)$ be the target data distribution. For simplicity, consider a forward diffusion whose noise coefficient depends only on time, as in standard score-based SDE formulations:

$$ dY\_t = f(Y\_t, t)\,dt + \sigma(t)\,dB\_t, \qquad Y\_0 \sim p\_{\text{data}}. $$

Let $p\_t(x)$ denote the marginal density of $Y\_t$. Under standard regularity assumptions, the time reversal of this process is again a diffusion. Instead of writing time backward from $T$ down to $0$, define

$$
X\_t := Y\_{T-t}, \qquad t\in[0,T].
$$

Then $X\_0\sim p\_T$, $X\_T\sim p\_{\text{data}}$, and $X\_t$ has marginal $p\_{T-t}$.

To expose the control structure [[9]](#references), define the reverse-time drift and diffusion coefficients

$$ \mu(x, t) := -f(x, T-t), \qquad \Sigma(t) := \sigma(T-t). $$

Now consider a family of controlled diffusions $X\_t^u$ driven by an arbitrary control field $u(x, t)$:

$$ dX\_t^u = \big(\mu(X\_t^u, t) + \Sigma(t) u(X\_t^u, t)\big)\,dt + \Sigma(t)\,dW\_t, \qquad X\_0^u \sim p\_T. $$

The goal is to choose $u$ so that the terminal law of $X\_T^u$ matches $p\_{\text{data}}$.

Now define the candidate value function

$$ V(x, t) := -\log p\_{T-t}(x). $$

This is the negative log-density of the reverse-time marginals, so its terminal value is

$$ V(x, T) = -\log p\_{\text{data}}(x). $$

To identify the PDE satisfied by $V$, recall that the forward marginals $p\_t$ solve the Fokker-Planck equation for $Y\_t$. Consequently, $\rho\_t(x) := p\_{T-t}(x) = e^{-V(x, t)}$ satisfies the reverse-time Fokker-Planck PDE

$$ \partial\_t \rho\_t = -\operatorname{div}(\mu\,\rho\_t) - \tfrac{1}{2}\operatorname{Tr}\big(\Sigma\Sigma^\top \nabla\_x^2 \rho\_t\big). $$

Substituting $\rho\_t = e^{-V}$, $\nabla\_x \rho\_t = -e^{-V}\nabla\_x V$, and $\nabla\_x^2 \rho\_t = e^{-V}(\nabla\_x V\nabla\_x V^\top - \nabla\_x^2 V)$ into that PDE and dividing by $-e^{-V}$ yields

$$ \partial\_t V = \operatorname{div}\mu - \mu \cdot \nabla\_x V + \tfrac{1}{2}\|\Sigma^\top \nabla\_x V\|^2 - \tfrac{1}{2}\operatorname{Tr}\big(\Sigma\Sigma^\top \nabla\_x^2 V\big). $$

To rewrite this as a control problem, introduce a control variable $u$ through the convex-conjugate identity for the quadratic function $g(y) = \frac{1}{2}\|y\|^2$:

$$ \tfrac{1}{2}\|y\|^2 = \sup\_{u\in\mathbb{R}^d} \left\{ u \cdot y - \tfrac{1}{2}\|u\|^2 \right\}. $$

Setting $y = -\Sigma^\top \nabla\_x V$ lets us rewrite the quadratic gradient term as

$$ \tfrac{1}{2}\|-\Sigma^\top \nabla\_x V\|^2 = \sup\_{u} \left\{ u^\top (-\Sigma^\top \nabla\_x V) - \tfrac{1}{2}\|u\|^2 \right\} = -\inf\_{u} \left\{ \tfrac{1}{2}\|u\|^2 + (\Sigma u) \cdot \nabla\_x V \right\}. $$

This is the key step: it replaces a quadratic gradient term with a linear one that can be interpreted as controlled drift.

Plugging this back into the PDE for $V$, multiplying by $-1$, and collecting the $u$-independent terms inside the infimum gives the finite-horizon HJB equation

$$ -\partial\_t V = \inf\_u \left\{ \tfrac{1}{2}\|u\|^2 - \operatorname{div}\mu + (\mu + \Sigma u)\cdot \nabla\_x V + \tfrac{1}{2}\operatorname{Tr}\big(\Sigma\Sigma^\top \nabla\_x^2 V\big) \right\}. \tag{3} $$

This PDE shows that $V(x,t) = -\log p\_{T-t}(x)$ is exactly the value function of a stochastic control problem with dynamics $X\_t^u$ and cost

$$ J(u; x, t) = \mathbb{E}\left[ \int\_t^T \left( \tfrac{1}{2}\|u(X\_s^u,s)\|^2 - \operatorname{div}\mu(X\_s^u,s) \right) ds - \log p\_{\text{data}}(X\_T^u) \;\middle|\; X\_t^u=x \right]. $$

The optimal control law $u^\*(x, t)$ is the minimizer in the HJB equation. From the quadratic optimization above, the minimizer of $\frac{1}{2}\|u\|^2 + u^\top (\Sigma^\top \nabla\_x V)$ is obtained by setting its derivative with respect to $u$ to zero:

$$ u^\* + \Sigma^\top \nabla\_x V = 0 \implies u^\*(x, t) = -\Sigma^\top(t)\nabla\_x V(x, t). $$

Since $V(x, t) = -\log p\_{T-t}(x)$, we have $\nabla\_x V = -\nabla\_x \log p\_{T-t}(x)$. Substituting this identity gives the exact optimal control law

$$ u^\*(x, t) = \Sigma^\top(t)\nabla\_x \log p\_{T-t}(x) = \sigma(T-t)^\top \nabla\_x \log p\_{T-t}(x). $$

Therefore the controlled drift becomes

$$
\mu(x,t)+\Sigma(t)u^\*(x,t)
=-f(x,T-t)+\Sigma(t)\Sigma(t)^\top \nabla\_x \log p\_{T-t}(x),
$$

which is exactly the reverse-time score correction.

Applying Itô’s formula to $V(X\_s^u, s)$ along an arbitrary controlled trajectory and then using the HJB gives the verification identity

$$ J(u; x, t) = V(x, t) + \frac{1}{2} \mathbb{E}\left[ \int\_t^T \| u(X\_s^u,s) - u^\*(X\_s^u,s) \|^2 ds \;\middle|\; X\_t^u = x \right]. $$

This identity is the control-theoretic backbone of diffusion models:

1. Depending on the parameterization, the network can predict either the score $s(x,t)=\nabla\_x\log p\_{T-t}(x)$ or the scaled control $u(x,t)=\Sigma^\top(t)s(x,t)$.
2. The verification gap is quadratic in the control error. Under the standard diffusion-model reparameterization used in practice, the resulting ELBO reduces to a weighted denoising score-matching objective [[9]](#references).
3. When $u=u^\*$, the gap vanishes and the terminal law of the reverse process matches the data distribution exactly.

So diffusion-based generative modeling can be viewed as a finite-horizon stochastic optimal control problem whose optimal policy is precisely the score-induced reverse-time drift correction.

References[#](#references)
--------------------------

[1] Jia, Yanwei, and Xun Yu Zhou. “q-Learning in continuous time.” Journal of Machine Learning Research 24, no. 161 (2023): 1-61.

[2] Jia, Yanwei, and Xun Yu Zhou. “Policy gradient and actor-critic learning in continuous time and space: Theory and algorithms.” Journal of Machine Learning Research 23, no. 275 (2022): 1-50.

[3] Hamilton-Jacobi-Bellman Equations,
Stochastic Differential Equations by Benjamin Moll <https://benjaminmoll.com/wp-content/uploads/2019/07/Lecture4_ECO521_web.pdf>

[4] Fleming, Wendell H., and H. Mete Soner. Controlled Markov processes and viscosity solutions. New York, NY: Springer New York, 2006.

[5] Yong, Jiongmin, and Xun Yu Zhou. Stochastic controls: Hamiltonian systems and HJB equations. Vol. 43. Springer Science & Business Media, 1999.

[6] Bellman, Richard. “On the Theory of Dynamic Programming.” Proceedings of the National Academy of Sciences 38, no. 8 (1952): 716-719. <https://doi.org/10.1073/pnas.38.8.716>.

[7] Bellman, Richard Ernest. An Introduction to the Theory of Dynamic Programming. Santa Monica, CA: RAND Corporation, 1953. <https://www.rand.org/pubs/reports/R245.html>.

[8] Kalman, Rudolf E. “Contributions to the Theory of Optimal Control.” Boletin de la Sociedad Matematica Mexicana 5 (1960): 102-119. <https://boletin.math.org.mx/pdf/2/5/BSMM%282%29.5.102-119.pdf>.

[9] Berner, Julius, Lorenz Richter, and Karen Ullrich. “An optimal control perspective on diffusion-based generative modeling.” Transactions on Machine Learning Research, 2024. <https://arxiv.org/abs/2211.01364>.

Appendix A: LQR Derivation[#](#appendix-a-lqr-derivation)
---------------------------------------------------------

**Ansatz.** Guess $V(x) = -\tfrac{1}{2}Px^2 - c$ with $P > 0$. Then $V'=-Px$, $V''=-P$.

**Generator.** With drift $f = \alpha x + \beta a$ and constant diffusion $\sigma$:

$$
\mathcal{L}^a V
=V'(\alpha x+\beta a)+\tfrac{1}{2}\sigma^2V''
=-Px(\alpha x+\beta a)-\tfrac{1}{2}\sigma^2P
=-\alpha P x^2-\beta P a x-\tfrac{1}{2}\sigma^2P.
$$

**HJB.** Substituting into $\rho V = \max\_a \{r + \mathcal{L}^a V\}$:

$$
-\tfrac{1}{2}\rho P x^2 - \rho c
=\max\_{a}\Big\{-\tfrac{1}{2}qx^2-\tfrac{1}{2}r\_a a^2-\alpha P x^2-\beta P a x-\tfrac{1}{2}\sigma^2P\Big\}.
$$

**Optimality in $a$.** The RHS is concave in $a$; set $\partial\_a(\cdot) = 0$:

$$
-r\_a\,a-\beta P x=0
\implies
a^\*(x)=-\frac{\beta P}{r\_a}\,x=: -Kx.
$$

**Riccati equation.** Substituting $a^\* = -Kx$ back and matching the $x^2$ coefficient and the constant:

$$x^2:\quad \rho P = q + 2\alpha P - \frac{\beta^2}{r\_a}P^2, \qquad \text{const:}\quad c = \frac{\sigma^2 P}{2\rho}$$

The first is the *discounted algebraic Riccati equation*. In the scalar case it is a quadratic in $P$. $\quad\blacksquare$

Appendix B: Merton Derivation[#](#appendix-b-merton-derivation)
---------------------------------------------------------------

**Ansatz.** Power-law value: $V(x) = \frac{A}{1-\gamma}\,x^{1-\gamma}$, $A > 0$. Then:

$$V'(x) = A\,x^{-\gamma},\qquad V''(x) = -\gamma A\,x^{-\gamma-1}$$

**Generator.** Using drift $\mu\_X x = [r\_f + \pi(\mu-r\_f) - k]x$ and diffusion $\sigma\_X x = \pi\sigma x$:

$$\mathcal{L}^a V = A\,x^{-\gamma}\cdot\mu\_X x - \tfrac{1}{2}\gamma A\,x^{-\gamma-1}\cdot\sigma\_X^2 x^2 = A\,x^{1-\gamma}\big[r\_f + \pi(\mu-r\_f) - k - \tfrac{1}{2}\gamma\pi^2\sigma^2\big]$$

**HJB.** Substituting and dividing through by $x^{1-\gamma} > 0$:

$$\frac{\rho A}{1-\gamma} = \max\_{\pi,\,k}\left\{\frac{k^{1-\gamma}}{1-\gamma} + A\big[r\_f + \pi(\mu-r\_f) - k - \tfrac{1}{2}\gamma\pi^2\sigma^2\big]\right\}$$

**Optimality in $\pi$.** FOC $\partial\_\pi(\cdot) = 0$: $\;A[(\mu-r\_f) - \gamma\pi\sigma^2] = 0$:

$$\pi^\* = \frac{\mu - r\_f}{\gamma\,\sigma^2}$$

This is the **myopic** portfolio rule — independent of wealth and time. Higher risk aversion $\gamma$ or volatility $\sigma$ reduces exposure.

**Optimality in $k$.** FOC $\partial\_k(\cdot) = 0$: $\;k^{-\gamma} - A = 0$, so $k^\* = A^{-1/\gamma}$.

**Solving for $A$.** Define the *certainty-equivalent growth rate* $M := r\_f + \frac{(\mu-r\_f)^2}{2\gamma\sigma^2}$. Substituting the optimisers back:

$$
\frac{\rho A}{1-\gamma}
=\frac{(A^{-1/\gamma})^{1-\gamma}}{1-\gamma}+A\big[M-A^{-1/\gamma}\big]
=\frac{A^{(\gamma-1)/\gamma}}{1-\gamma}+AM-A^{(\gamma-1)/\gamma}.
$$

Multiplying by $1-\gamma$ and collecting terms gives

$$
\rho A=(1-\gamma)AM+\gamma A^{(\gamma-1)/\gamma}.
$$

Since $A>0$, divide by $A^{(\gamma-1)/\gamma}$ to obtain

$$
A^{1/\gamma}=\frac{\gamma}{\rho-(1-\gamma)M}.
$$

Therefore

$$
A = \left(\frac{\gamma}{\rho - (1-\gamma)M}\right)^\gamma, \qquad k^\* = \frac{\rho - (1-\gamma)M}{\gamma}
$$

The denominator $\rho - (1-\gamma)M$ must be positive — this is the **feasibility condition** ensuring lifetime utility is finite. With our parameters: $M \approx 0.04563$, so $k^\* \approx 0.0478$. $\quad\blacksquare$

Appendix C: Non-autonomous and Finite-Horizon Cases[#](#appendix-c-non-autonomous-case)
---------------------------------------------------------------------------------------

Let the dynamics and reward depend on time:

$$
dX\_t=f(t,X\_t,a\_t)\,dt+\Sigma(t,X\_t,a\_t)\,dW\_t,\qquad r=r(t,x,a).
$$

For the discounted infinite-horizon problem, define the time-dependent value

$$
V(t,x):=\sup\_\pi \mathbb E\Big[\int\_t^\infty e^{-\rho(s-t)} r(s,X\_s,a\_s)\,ds\ \Big|\ X\_t=x\Big].
$$

Then the time-dependent generator is

$$
\mathcal L\_t^a \varphi(x)=\nabla \varphi(x)^\top f(t,x,a)+\tfrac12\mathrm{Tr}\big(\Sigma\Sigma^\top(t,x,a)\nabla^2\varphi(x)\big),
$$

and the HJB becomes

$$
\rho V(t,x)=\max\_{a\in\mathcal A}\Big\{r(t,x,a)+\partial\_t V(t,x)+\mathcal L\_t^a V(t,x)\Big\}.
$$

Equivalently,

$$
-\partial\_t V(t,x)=\max\_{a\in\mathcal A}\Big\{r(t,x,a)+\mathcal L\_t^a V(t,x)\Big\}-\rho V(t,x).
$$

In the autonomous case, $V(t,x)$ is time-independent, so $\partial\_t V=0$ and you recover (1).

For the finite-horizon deterministic case, set $\Sigma\equiv 0$ and define

$$
V(t,x):=\sup\_{a\_\cdot}\left[\int\_t^T r(s,X\_s,a\_s)\,ds+g(X\_T)\,\middle|\,X\_t=x\right].
$$

Then

$$
-\partial\_t V(t,x)=\sup\_{a\in\mathcal A}\left\{r(t,x,a)+\nabla\_x V(t,x)^\top f(t,x,a)\right\},
\qquad V(T,x)=g(x).
$$

Writing $r=-L$ and

$$
H(t,x,p):=\sup\_{a\in\mathcal A}\{p^\top f(t,x,a)-L(t,x,a)\},
$$

this becomes

$$
\partial\_t V(t,x)+H\bigl(t,x,\nabla\_x V(t,x)\bigr)=0,
\qquad V(T,x)=g(x),
$$

which is the classical Hamilton-Jacobi form.
