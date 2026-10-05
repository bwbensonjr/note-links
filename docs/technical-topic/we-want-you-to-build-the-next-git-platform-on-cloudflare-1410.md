---
id: 1410
url: https://blog.cloudflare.com/next-git-platform-on-cloudflare/
title: We want you to build the next Git platform on Cloudflare | Cloudflare Blog
domain: blog.cloudflare.com
source_date: '2026-10-02'
tags:
- github-repo
- ai
- devops
- distributed-systems
summary: Cloudflare is launching a competition to challenge developers to build the
  next-generation Git platform designed for AI agents rather than humans, leveraging
  Cloudflare's new Artifacts versioned filesystem. The platform needs to handle coordination
  and code review for hundreds or thousands of agents working simultaneously on the
  same codebase, moving beyond traditional Git concepts built for human collaboration.
  Cloudflare has released new Artifacts capabilities including Workers integration,
  event subscriptions, data jurisdiction controls, and metrics, with submissions due
  by October 14, 2026, offering $25,000 in credits and travel to Cloudflare Connect
  for top projects.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# We want you to build the next Git platform on Cloudflare | Cloudflare Blog

![](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3VGDDQQHKX35297BEXJZ5H0.01M3VGDEMW20N9CFDP5TEPV5EJ.png&w=1999&h=1125&f=webp&fit=cover&position=center)![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/////v3+5+nx2t7r4+bw8/P29/X07+7q/////v3/5Ofy0tns2N/x6e348fL27u7r////////4+f1zdbuz9r04Oj77PD57u/v////////5+v5z9nyz9v43un/7PL98vPz////////8fT+3OP32uT95/D/8/j/+Pn5/////////P3/7fD97PL/9vv//v/////+////////////+vv/+/3/////////////////////////////////////////////)

GitHub was built for a world where humans write code, organize it into repositories, and collaborate through branches, commits, issues, and pull requests.

But the next generation of software is going to be built differently because it is going to be built by a different kind of developer: agents.

Agents are already writing more code than ever before — they’re fixing bugs, building features, writing tests, reviewing changes, updating dependencies, and doing the routine maintenance required to keep an application running.

So in this new world where you have hundreds, or even thousands, of agents working on the same codebase at the same time, what does the foundation look like?

How do agents know what other agents are working on? What happens when they make conflicting changes? How do you review everything they produce? How do you keep track of not just what changed, but *why* a change was made?

And so the burning question is: **What does the next GitHub look like?**

We want you to help us answer it, by building it out.

Earlier this year, we launched [Artifacts](https://blog.cloudflare.com/artifacts-git-for-agents-beta/), a versioned filesystem that speaks Git and can scale to millions of repositories. From the start, we designed Artifacts as a set of programmable primitives that developers could use to build their own products, workflows, and abstractions.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAAnlpCoFtFol1Kol5LnltLmFhNkFZWilZgq2dMrGlQrWtWrWxZq2tXpWdYm2RgkmJpunVXundbuXliuntluXpjtHZiqXJpnG5yx4FfxoFixINpxIRrxYRpwYBotnxtqHh1z4djzodly4dpyohqy4doyYVov4Frsnxx1Ipk0olkzodkzIZjzYZizIVjxYFlu31o1otk04lizoVezIJbzYNbzYNdyIBewHxe1otk04hhzoRby4FXzIFYzYJayX9bwntZ)![](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3SQC6HRKEPPV90RWXN9CTKR.png&w=715&h=396&f=webp&fit=cover&position=center)

Artifacts provides the foundation: repositories that can be created and forked programmatically, versioned storage for code and agent context, and the Git operations agents already know how to use.

With that foundation in place, you can focus on the layer above it: how agents coordinate their work, how changes are reviewed and merged, and what the developer experience should look like when hundreds or thousands of agents are working on the same codebase.

That is the layer we want you to build.

Now that Artifacts is in open beta, [we’re holding a competition](http://cloudflare.com/git-competition) to see who can build the next Git platform on Cloudflare using Workers and Artifacts.

Artifacts is in open beta. Here’s why you should build on it
------------------------------------------------------------

When we launched Artifacts, our goal was to make it possible to create a repository for every agent, session, task, or user — and to do that at the scale agents require.

Since then, we’ve seen developers use Artifacts in a range of ways: Vibe-coding platforms are using it to store the projects their users create. Developers are using it to persist the code and context from agent sessions. Others are creating isolated repositories, so multiple agents can safely work from the same starting point and compare or merge the results later.

Here are some new capabilities we’ve added since the initial launch.

### Deploy Artifacts repos to Workers

You can now connect an Artifacts repository to a Worker through [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/artifacts-integration/). When you or an agent pushes code to the Artifacts repository, Cloudflare will build the project and, for the production branch, deploy the updated Worker. Pushes to other branches automatically create or update [Workers Previews](https://developers.cloudflare.com/workers/previews/), giving you an isolated, shareable version of your Worker where you can test changes before they go live.

You can connect an existing Worker to an Artifacts repository or start a new project and automatically store it in Artifacts.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA+/v69/f38fHx7+/v8/P09/f39PTz6+vq/v79+/v69PT08/Pz9/f4+vr79/f37u7u///////++fn49/f3+/v8/v7/+/v78vLy////////+/v7+vr6/v7//////v7+9vb2/////////Pz8+/v7////////////+Pj4////////+/v7+vr6////////////+vr5////////+fn5+Pj5////////////+vr5////////+Pj49/f4//7/////////+vr5)![](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3SQC8RKCYFADSHXNX2XR1XF.png&w=715&h=559&f=webp&fit=cover&position=center)

### Manage Artifacts directly from Workers

You can interact with Artifacts repositories directly from a Worker using an [Artifacts binding](https://developers.cloudflare.com/artifacts/api/workers-binding/) to create or fork repos, inspect files and commits, and issue repo-scoped Git tokens. This makes your Git workflow programmable. When a new task arrives, a Worker can fork the project for an agent, read the files it needs for context, and give it a repository to work in. When the agent pushes a change, your automation can inspect the result and start a review. You define those steps in code to fit how your agents work.

For example, here’s how to fork a project for a new agent task and read its `AGENTS.md` for instructions:

```
using project = await env.ARTIFACTS.get("my-project");
const { defaultBranch } = await project.info();
const workspace = await project.fork(`task-${crypto.randomUUID()}`);

using repo = await env.ARTIFACTS.get(workspace.name);
const instructions = await repo.readFile({
  ref: defaultBranch,
  path: "AGENTS.md",
});

const agentTask = {
  remote: workspace.remote,
  token: workspace.token,
  instructions: instructions ? await instructions.text() : null,
};
```

### React to every change with event subscriptions

Artifacts publishes events whenever a repository is created, imported, forked, deleted, pushed to, cloned, or fetched. You can subscribe to these events to decide what happens next: run CI, kick off a code review agent, or deploy a change.

For example, you can subscribe to Artifacts push events and have a Worker start a code review workflow for each push. The Worker passes the repository, branch, and new commit to the Workflow, giving a review agent the context it needs to inspect the change:

```
export default {
  async queue(batch, env) {
    for (const message of batch.messages) {
      const event = message.body;
      if (event.type !== "cf.artifacts.repo.pushed") continue;

      await env.REVIEW_WORKFLOW.create({
        params: {
          namespace: event.source.namespace,
          repo: event.source.repoName,
          ref: event.payload.ref,
          commit: event.payload.after,
        },
      });
    }
  },
};
```

### Data jurisdiction for Artifacts repos

You can now [choose where Artifacts stores and processes](https://developers.cloudflare.com/artifacts/guides/data-localization/) your repository data. Set a U.S. or EU jurisdiction when you create a namespace, and every repository created in that namespace will automatically follow the same restriction.

```
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --json '{"namespace":"my-eu-namespace","jurisdiction":"eu"}'
```

### View Artifacts metrics

You can now see metrics for your Artifacts repositories in the Cloudflare dashboard. For each repository, you can now see total operations, pulls, pushes, errors, and error rate, helping you understand how the repository is being used and spot failures. You can also query [Artifacts metrics](https://developers.cloudflare.com/artifacts/observability/metrics/) directly to build your own dashboards or monitoring.

![](data:image/bmp;base64,Qk32BAAAAAAAADYAAAAoAAAACAAAAAgAAAABABgAAAAAAMAAAAATCwAAEwsAAAAAAAAAAAAA/e7r+e3r8evr7+7v9PP1+Pb39PLy6unq//f1/fTz9PDv8fDx9vX3+/n69/X27Ozs//////389/X18/Pz+fn6/v3++vn67vDw////////+/v69vf3/Pz9/////f7+8vTz/////////v7++vv7////////////9Pf2/////////////P3/////////////9vn4/////////////v//////////////+Pv5////////////////////////////+Pv5)![](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3SQC9MA49HNQD82GBG58EDM.png&w=715&h=466&f=webp&fit=cover&position=center)

### Pricing

Artifacts pricing is based on repository operations and the amount of data stored. We will begin billing for Artifacts usage on October 15, 2026.

Competition: Build the next Git platform on Cloudflare
------------------------------------------------------

We want you to build your vision for the Git platform of the agentic era using Cloudflare Workers and Artifacts.

You could rethink repositories, branches, pull requests, worktrees, code review, and merge conflicts — or build new ways to preserve agent context, compare multiple changes at the same time, and decide which one should ship.

We aren’t looking for GitHub as it exists today with agents added on top. At a minimum, we want to see multiple agents working on changes concurrently. Beyond that, we want you to get creative — what you think comes next.

### How to enter

Submit:

* A 5-10 minute video demonstrating what you built, what it enables agents and developers to do, and how it works
* A link to the source code, which must be provided under a permissive open source license (MIT, Apache, BSD)
* Instructions for running or trying the project

### Deadline

[Submissions](http://cloudflare.com/git-competition) are open until October 14, 2026.

### Why should you participate?

We’ll select the top three projects and fly up to two members from each team to San Francisco to attend [Cloudflare Connect](https://www.cloudflare.com/connect/) and show what they built.

The first-place team will also receive $25,000 in Cloudflare credits, along with invitations to the VIP speaker dinner on Monday night at Connect.

Get started
-----------

Artifacts is available in open beta to customers on the Workers Paid plan.

Get started with your coding agent:copy the prompt below to set up your first Artifacts repository and start pushing code to it.

Copy promptCopy promptPrompt copied!

You can view or create the Artifacts repositories in the [dashboard](https://dash.cloudflare.com/?to=/:account/workers/artifacts) or if you’re looking to learn more, check out the [documentation](https://developers.cloudflare.com/artifacts/).

![]()

Related tags
------------

[Birthday Week](/tag/birthday-week/)[Developers](/tag/developers/)[Workers](/tag/workers-1/)

Follow on Social Media

* ![Cloudflare](/images/placeholder__cloudflare.png)Cloudflare
* ![Dina Kozlov](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49DZ20ZY95S71GB0FPG6GC.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Dina Kozlov](/author/dina/)
* ![Zebulon Piasecki](/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01M3SPNPQ4FRWZZG3GWEV0VY2J.01M3SPNRCTC9WW528APGP7F8BP.jpg&w=64&h=64&f=webp&fit=cover&position=center)[Zebulon Piasecki](/author/zeb/)

Subscribe to receive notifications of new posts
-----------------------------------------------
