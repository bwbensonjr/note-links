---
id: 30
url: https://www.thecodedmessage.com/posts/pl-features/
title: 'What Features Should Rust Include? Part I: Not Inheritance. :: The Coded Message'
domain: www.thecodedmessage.com
source_date: '2026-01-07'
tags:
- rust
- compilers
summary: This article discusses programming language design principles, arguing that
  Rust deliberately excludes inheritance not out of tradition but through rigorous
  feature evaluation. The author contends that good language design requires features
  to work cohesively together, respect core invariants, and clear a high bar of necessity—prioritizing
  clarity and collective engineering over individual convenience. Using inheritance
  as an example, the piece illustrates how Rust, influenced by functional programming
  rather than OOP, evaluates potential features neutrally rather than assuming they
  should be included by default.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# What Features Should Rust Include? Part I: Not Inheritance. :: The Coded Message

[What Features Should Rust Include? Part I: Not Inheritance.](https://www.thecodedmessage.com/posts/pl-features/)
=================================================================================================================

2025-07-19
:: Jimmy Hartzell

#[programming](https://www.thecodedmessage.com/tags/programming/) 
#[computers](https://www.thecodedmessage.com/tags/computers/) 
#[Rust](https://www.thecodedmessage.com/tags/rust/) 
#[OOP](https://www.thecodedmessage.com/tags/oop/) 
#[Beyond OOP](https://www.thecodedmessage.com/tags/beyond-oop/) 
#[Rust Features](https://www.thecodedmessage.com/tags/rust-features/) 

Programming language design, like API design, and computer UX design
(especially for technical tools like build systems and admin systems) is a
difficult form of engineering, bridging computer science and cognitive
science. Sometimes, it’s more art than science, because building systems
that other technical workers will use comes with nearly infinite trade-offs
and judgment calls.

The effort and quality matter too. Different programming languages have
different strengths and weaknesses. Some programming languages are hard to
use correctly, like C++. Some are easy to write, but hard to then read and
maintain, like Perl. Some programming languages are great for one-off
scripts where you’re the only user, like Python, and others enforce that you
follow reliable engineering principles, like Rust.

And some programming languages are just [better than
others](https://www.thecodedmessage.com/posts/best-programming-language/).
C++11, for example, is miles better than previous versions of C++ – what do
you even do with standard collection types if you can’t do move operations?
I would also argue – and have argued – that Rust is similarly a better C++
than C++ at almost any use case (partially because its move operation [makes
more sense](https://www.thecodedmessage.com/posts/cpp-move/)).

This mostly has to do with what features are available in a programming
language. Pre-C++11 versions of C++ lacked a feature (move operations) that
turn out to be essential in combination with other features (such as RAII).
Some features give the user more power, like move operations or inheritance,
whereas others help the user by preventing them from accidentally doing
something that’s probably a mistake, like linting or type checking.

How to Decide[#](#how-to-decide)
================================

So, how do we make decisions on which features to include and
which to exclude?

A good programming language has features
that work well together, where you can use them in combination
with each other and everything makes sense, and where it’s
pretty easy to determine which feature to use for a given situation.

Some are lightweight, like C, which I consider a good programming language.
Some are more feature-heavy, like Rust, or Haskell. But in all of these
cases, the feature set is curated, as is each individual feature, to do more
good than harm.

A bad programming language has overlapping, incompatible features. It has
so many features that no one knows all of them well, so that reading someone
else’s code can end up looking like reading another programming language
because they use a different subset, or so that you have to consider every
feature when writing your code. Or, it has missing features that really are
implied by features it already has, or that fix gaps for which the
work-arounds are ugly.

Beyond just increasing cognitive load, there are also often specific
downsides to including a feature, especially a complicated one. In a safe
language, complex features can introduce safety issues, including ones
missed by the language designers. In many languages, features can also be
“viral” – once you have `async`, for example, it propagates up the function
chain through [function coloring](/posts/async-colors). And once you’ve
solved a problem one way, you foreclose better solutions.

A programming language needs to have invariants, things programmers can
always rely on. In Rust, all types are trivially moveable. In Rust, you
cannot override the assignment operator (`=`), so you’ll never have to guess
what it means in context. In Java, (at least traditionally) all types but a
short list have reference semantics, and alias by default. New features
have to respect these old invariants.

All of this together means, that there is a bar that every feature in a
well-designed programming language has to clear. It’s not enough that a
feature might ever be a more convenient way to express a use case, it also
has to be a clearer way, a way that combines well with the other features of
the programming language. If the programming languages already has other
features to express that use case, how does the new feature compare?

TMTOWDI vs One True Way[#](#tmtowdi-vs-one-true-way)
====================================================

Having only one major feature per use case is a controversial principle.
Famously, Perl disowned it, with its motto TMTOWTDI, “There’s more than one
way to do it,” which among other decisions led to Perl being derided (with a
fair amount of truth) as a “write-only programming language.” Python,
which entered into existence as a “scripting language” at a time when
Perl was the king of scripting languages, explicitly took the opposite
approach of there being “one true way.”

I can see the advantages of the Perl approach. I used to really like Perl,
back when it was a serious (perhaps *the* serious) option for many use
cases. Programming with a smörgåsbord of choices is super pleasant, turning
the experience into a matter of self-expression, designing your own idiom
out of the subset of features that you choose, out of comfort or just raw
coolness factor.

But programming in most settings – and certainly in the systems programming
settings for which Rust is primarily designed – is a collective rather than
an individual task. Systems programming specifically is almost always an
exercise in collaborative engineering, not in self-expression or convenience
or customization to our idiosyncratic preferences of aesthetic/convenience.
Programmer choice for its own sake is of marginal value at best, and a
positive hindrance in many circumstances.

In light of this, Rust goes more with Python than with Perl. The programming language
is trying to provide a feature set that works well together, not
a feature set with every bell and whistle that some other programming
language might have. Rust values clarity and readability over
convenience, and so if a feature would just save a few lines of
typing, that’s probably not a good enough reason to include it.

There are some overlapping features in Rust, but few are truly redundant for
Rust’s core use case as a systems programming language. Rust requires
control over memory layouts and performance, and many overlapping features
(such as static and dynamic polymorphism, or arrays and vectors) have
different memory layout and performance properties. The differences in
semantics reflect real differences in implementation strategy. And, to the
extent that they can be, these features are implemented in compatible ways:
static and dynamic polymorphism both use traits (with some traits just [not
eligible](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility)
for dynamic polymorphism), and arrays and vectors can both be used with
slices and iterators.

Inheritance in Rust?[#](#inheritance-in-rust)
=============================================

I am being somewhat abstract here, so let me give an example: Inheritance.

You may come from an OOP background, as many programmers do.
You may also have a *status quo* bias in how you think about
programming, as most humans do (it’s an adaptive cognitive strategy,
even if it’s not always helpful). From such a perspective, it’s
easy to assume that inheritance should be included in a programming
language unless there’s a strong reason to exclude it.

But Rust does not come from an OOP tradition. It is heavily influenced by
Haskell, a functional programming language. Its other major influence, C++,
has been moving away from OOP for a long time, adding functional features
and new forms of polymorphism based on templates rather than inheritance and
late binding.

So when the designers of Rust consider features like inheritance, they
consider them from a more neutral perspective. Being a pillar of OOP is not
a strong reason to include it. Instead, it’s treated like every other
feature.

If anything, the *status quo* bias here reads in the opposite direction.
The *status quo* for Rust is that Rust currently does not include
inheritance. The burden of proof on someone saying that Rust should
include a feature is on the person advocating for the feature.

And there is a high bar for including new features in Rust, and for good
reason. Inheritance doesn’t clear this bar. Everything inheritance
provides, other features can do just as well, usually better. Maybe there are
a few edge cases where inheritance saves you a little bit of typing, but
there are also plenty of cases where inheritance is overkill and both a sign
of and a cause of overengineering.

Features Redundant to Inheritance[#](#features-redundant-to-inheritance)
------------------------------------------------------------------------

When I program in C++, I use inheritance sometimes, in spite of [valid
criticisms against it within the C++
world](https://learn.microsoft.com/en-us/shows/goingnative-2013/inheritance-base-class-of-evil).
When I program in Rust, I never miss it, because of other features Rust
already has for every use case. In order to justify including inheritance in
Rust, it would have to provide something that these other features don’t.

I use inheritance when I need to create a type where the data might have
many possible shapes. For example, I might want a base class
`ProtocolMessage`, with subclasses for every concrete message type.
Then, there would be a polymorhpic method to serialize each method’s
particular fields, perhaps called by a non-polymorhpic method that
also serializes header fields and sends them over a wire.

In Rust, I would use an `enum` for this, or a combination of a `struct`
and an `enum`. Instead of a polymorphic method, I would use a `match`
statement. I like this structure much better.

I also use inheritance in C++ to implement dynamic polymorphism. Though
other techniques exist, especially in more modern versions of C++,
inheritance has built-in programming language support and is therefore less
work. (Also, some of the other techniques still use inheritance as an
implementation layer.) When doing so, I usually just have virtual and
non-virtual methods in the base class, and no fields – essentially using
the subset of C++ inheritance that is an exact match for Rust dyn-compatible
traits.

Finally, I use inheritance in C++ to interact with existing
inheritance-based designs. These are usually situations where
inheritance is set up by a framework library, and the framework
library expects you to use inheritance to fill in your implementation
details of something. This might be handlers for an event dispatcher,
or screens or widgets in a GUI, or individual protocol implementations
in a domain-specific framework for networking or device drivers.

If I was designing my own such framework, out of respect for convention and
what C++ programmers are used to, I would consider using inheritance. Some
of these even involve putting fields in base classes that are mostly used as
interfaces, and in such a case I can see how that’s a convenient factoring.
It’s never necessary, though, so I probably wouldn’t, making my preferred
version of this use case a special case of using C++ inheritance to
implement what Java calls an `interface` and which Rust would call a
`dyn`-compatible `trait`.

In none of these use cases am I engaging with principles from OOP theory
like the [Liskov Substitution
Principle](https://en.wikipedia.org/wiki/Liskov_substitution_principle). I
am instead engaging with programming without reference to such principles,
understanding what inheritance does and striving to use it appropriately.

In the first use case, I’m using inheritance within the internal logic of my
code, but I am mentally treating it like a sum type, albeit a strange and
heap-heavy implementation of sum types. This pattern happens to align with
the Liskov substitution principle, but only because sum types are a similar
concept, if anything a bit more rigorously and intuitively defined.

If I do use inheritance as an extension of sum types, I get something that
sum types don’t give me: the ability for other modules of code to add their
own additional variant. This is a mixed blessing from my point of view –
usually, I’d rather they not, and I dislike that there’s no single place
where all the variants are listed. If I wanted this property in Rust,
I may choose to implement a `dyn`-compatible `trait`, which leads
to the second use case.

For the second use case, I use inheritance as C++’s version of
`dyn`-compatible traits. This is a type of dynamic polymorphism,
and I use it because I want dynamic polymorphism. As long as I
do not include state in my base class, in my “interface,” if you
will, I am in line with the Liskov Substitution Principle.

But again, that is not my conscious reason for not putting fields
in my base class. The conscious reason is that adding fields
and defining a polymorphic interface are different things, and
I should not constrain my polymorphic interface to types that
happen to have certain fields.

For any use case for fields in traits, there are just better ways already
available to express it. If implementors of the polymorphic interface
usually benefit from having such fields, I can provide a `struct` for them
as a tool, and let them not use it where appropriate. If I want those fields
for my implementation, I can make my own wrapper `struct` and put my fields
in that wrapper `struct`. In either case, this makes my intent clearer.

For the third use case, I don’t have any control over whether people
put fields in their base classes. But if I were implementing a framework,
I would not, for the reasons I already mentioned.

So, in all my personal use cases for inheritance, Rust provides other (I
would argue, better) tools. In my experience, use cases of inheritance
either fall into one of these categories, or they are an instance of someone
using inheritance problematically (or both). But I am open to other
use cases for inheritance – please comment here with additional ones,
and I will address (at my own schedule) how to implement that sort
of inheritance in Rust.

If you do this, please be specific. A lot of examples are too vague to
explain how to translate into Rust. Include information about what the base
class is, what the derived class is, and what sort of operations clients of
this hierarchy would perform. A short code example is extra helpful. I
reserve the right to ask clarification questions, or to explain why
it reduces to one of the use cases I’ve already discussed.

I suppose if I set up this challenge, I should mention that a fourth use
case for inheritance is just what I would use composition for – putting all
the fields in one `struct` in another `struct` as well. In this case, the
answer is simple and available in C++ too: Put all the inner fields in the
outer `struct`. Said another way: Use composition instead.

The distinction between composition and inheritance is dubious.
That’s what I spend my original post talking the most about,
but I can summarize in brief now.

If you’re using inheritance just to put all the fields from one product type
into another, composition is equivalent and better. The downsides are
superficial. If composition involves a little bit of extra typing, it’s
worth it in my mind for the extra clarity. If it breaks OOP concepts of
encapsulation to allow direct field address, then you can write methods on
your wrapper, or just adjust to [different concepts of
encapsulation](/posts/oop-1-encapsulation).

No Need for Inheritance[#](#no-need-for-inheritance)
----------------------------------------------------

Given these better tools for the use cases of inheritance,
there is no need to add inheritance to Rust. It would be truly
redundant.

Rust already supports vtables in its implementation of `dyn`-based “trait
objects” in Rust. (I was hoping, in writing this, that they’d come up with a
new name for trait objects, just like they’d replaced the needlessly
judgmental and misleading term “object safe” with “`dyn`-compatible,” but
this seems to not have happened – yet.) If it supported OOP-style
inheritance, would this implicitly define a trait, or would it be
yet another syntax for a different memory layout for vtables?
If someone wanted to use dynamic polymorphism, how would they decide
which pattern to reach for?

This isn’t just a matter of how to give programmers practical
advice. Different programmers would, in practice, choose different
options. Teams would need to make policies, and skilled
Rust programmers would need to be conversant in both conventions.
Rust is already a complicated language, straining the bounds
of human cognitive load. We don’t need more features in the mix.

Similarly, Rust already supports composition. Having another syntax that
accomplishes the same thing would similarly just increase confusion and
decrease consistency. Some would use inheritance even when it is not
justified, and others would avoid it in line with present Rust usage, and
the principle of “composition over inheritance” which is already common in
languages that offer the feature.

In the end, inheritance would make the language more confusing, for a
feature with no distinctive use cases.

Foggy Semantics[#](#foggy-semantics)
------------------------------------

For all OOP advocates claim OOP is intuitive, inheritance is confusing.
Inheritance is hard to teach to new programmers. Experts disagree about what
the rules are on when to use it. Programmers regularly use it
in confusing and arguably incorrect ways.

Its overlap with composition is obvious even to students. Intro CS students
are taught the distinction between “has-a” and “is-a,” and navigate it
poorly because of how unintuitive it is. It’s easy to get wrong, and
the consequences of getting the feature wrong are terrible design.
Rust tries to direct people towards good design, as part of Rust’s
general focus on safety and on reliable engineering.

More sophisticated theory, like the Liskov Substitution Principle, might
clear up the issue for some, but honestly the principle is arcane, and to me
seems as subjective as “is a” vs “has a,” while requiring even more
cognitive load. To me, that doesn’t say that people need to be educated
more. It just makes me skeptical that we need a feature that requires this
much education. Why have a feature that’s so easy to use wrong, and so hard
to use right?

Rust does already have features that are hard to use effectively.
But I don’t think this works as an argument in favor of including more such
features, like inheritance. To the contrary, it’s a reason
to be discriminating in including more such features.

Most of the difficulty of Rust’s existing features are necessary for the
feature. These more confusing features, in turn, are necessary
for Rust’s performance goals. There’s enough actual complexity in
how computers work that we don’t need to introduce more for philosophical
reasons.

For example, the borrow checker is necessary to implement memory safety. Rust rejects
reference counting and mark-sweep garbage collection in favor of the
zero-overhead strategy of single ownership. Similarly, Rust allows
references to the stack, and even references from the heap into the
stack. The borrow checker is the price we pay to implement these
essential features safely, and Rust constantly works to make it
more ergonomic and reduce false positives.

The ban that Rust puts on mutable aliasing prevents many common
programming mistakes. Sure, it makes programming more complicated
and increases cognitive load, but it prevents soundness issues.
The amorphous rules programmers have to follow in languages
that allow mutable aliasing have even more cognitive load.
At least Rust enforces its rules on aliasing and gives you an error
if you violate them, rather than just letting programmers write
buggy or even unsound software.

Traits are designed to allow monomorphization, getting the performance of
C++-style templates but with tools to make sure they’re used correctly. Most
of the complexity of traits comes from forcing users to be clear about
function signatures, a desirable outcome overall.

What does the distinction between inheritance and composition give you?
There’s enough essential complexity in systems programming that we
don’t need to introduce another layer just to make OOP theorists happy.

Responses to Criticism[#](#responses-to-criticism)
==================================================

I was criticized in my [previous post on this
topic](/posts/oop-3-inheritance) for not engaging with the Liskov
substitution principle, and for a few other things. I want to respond to
some common criticisms I’ve seen, on this post and elsewhere.

Why did I talk about “is a” and “has a” in the previous post, instead of the Liskov Substitution Principle?[#](#why-did-i-talk-about-is-a-and-has-a-in-the-previous-post-instead-of-the-liskov-substitution-principle)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To clarify, my goal in my previous post in discussing “is a” and “has a”
was to engage with how people actually use and talk about
inheritance in practice, because that’s how people would use
it in Rust if Rust had it. I’ve heard many people talk about
“is a” vs “has a,” and I’ve never heard of the Liskov substitution
principle outside of comments like this.

But people have brought it up, so I’ll bite! Let’s look at the Liskov
substitution principle:

> Subtype Requirement: Let ϕ(x) be a property provable about objects x of
> type T. Then ϕ(y) should be true for objects y of type S where S is a
> subtype of T.

This is very difficult to understand, let alone to prove. You want
a programming language feature that requires engaging with this
sort of definition to use correctly?

OK, let’s look at this translated into plain English in a [typical article
about the
principle](https://stackify.com/solid-design-liskov-substitution-principle/):

> The principle defines that objects of a superclass shall be replaceable
> with objects of its subclasses without breaking the application.

OK, that’s a little better. I’m going to engage with this version
of the definition. Then, I’m going to return to the original
definition, and try to argue that what I’ve reasoned still
applies.

So, to me, the key part of this definition is “shall.” This is a requirement
for the programmer to follow. If the programmer does not follow this
requirement, bad things will happen. The program will not work as designed,
and the programmer will face criticism for misusing inheritance.
Readers of the code will be confused by the use of inheritance,
and the code will be unmaintainable and fragile.

That is not in line with the goals of Rust. The goals of Rust are to create
features that are hard to use incorrectly, and easy to use correctly. This
is the opposite of that – instead, there is a difficult to understand
principle that you have to apply to know that you are using the feature
correctly.

This version of the definition has a vague rule for when to use inheritance:
Use it when replacing objects of the superclass with objects of the subclass
won’t break the application. Well, sure, but when is that? The more rigorous
version tells us it’s when every provable property that holds for the
superclass holds also for the subclass, which while much more
formal-sounding, is still not very easy to apply. The informal paraphrase
actually seems about right, as vague as it is.

Whenever Rust sees a rule like this, generally Rust tries to create concrete
rules to enforce them so the programmer can use the feature safely. So if
Rust had a feature like inheritance, Rust would create conservative rules to
avoid violations of this principle.

So, my gut reaction to this rule is, this feature is hard to use safely if
it has a rule like this. My secondary reaction is, inheritance would be fine
to include in Rust, if someone could just enforce this rule. This rule is so
vague that the only way to enforce it would be to allowlist good use cases
for the feature that we know don’t violate the rule. At that point, these
use cases might as well be different features.

And that, I would argue, is exactly what Rust does. Those features just
aren’t called “inheritance,” and don’t really look like inheritance. And
that’s fine. Rust has `dyn`-compatible traits for one use case of
inheritance, which is constrained so as to never violate this rule. Rust
also has `enum` types, which are similar to inheritance in that they allow
multiple concrete layouts in a single type, but constructed in such a way
that makes it hard to violate this rule.

Rust then leaves it there. Rust doesn’t allow some other forms of
inheritance, exactly because it has no way of enforcing that it follows this
rule, which is important for using inheritance correctly. If there are other
use cases that should be on the allowlist, perhaps Rust can add additional
features for those.

Aren’t composition and inheritance just different tools?[#](#arent-composition-and-inheritance-just-different-tools)
--------------------------------------------------------------------------------------------------------------------

For me, as I describe, inheritance is more like an awkward multitool.
It’s part hammer (composition), part screwdriver (sum type), part
toothpick (interface/trait), and part foot-gun. Unlike a good multitool,
however, it’s impossible to use one tool without using the others.
Rust has discerned the individual different valid use cases for
inheritance, and given programmers more appropriate tools to choose
between.

Why should Rust “forbid” inheritance? Shouldn’t the programming language offer the choice of inheritance?[#](#why-should-rust-forbid-inheritance-shouldnt-the-programming-language-offer-the-choice-of-inheritance)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First off, “forbid” is a misleading word here. Rust doesn’t go scanning your
code for patterns that look like inheritance implemented manually. You could
even implement an `extends!` macro that provides inheritance as a feature,
if you want, building it off of composition and traits, or maybe
`#[repr(C)]` and some internal unsafe casts. Rust will not stop you.

Rust just doesn’t offer inheritance as a feature. It’s not some obvious
feature built into the structure of the universe that you are entitled to in
a programming language by natural law. It’s just a feature that Rust
chooses not to provide, along with many other features that other
programming languages have that Rust doesn’t have.

Choices are sometimes good, sometimes bad. Rust is designed primarily as a
systems programming language for serious, collaborative projects, and so it
regulates the choices programmers make. It curates good practices, and
intentionally bans bad ones, like using unsafe features without tagging them
with the `unsafe` keyword.

I have seen this criticism many times. It seems compelling on a first
read, because who can be against choice? I suspect there is a conflation
between “choice” as a design principle within a programming language,
and “choice” as part of what it means to be human.

Free choice is an important value to me, on a human level. Choice,
freedom, liberty, whatever you want to call it, is part of what
it means to be human. However, the correct level of application of
that principle is at a human level, not within a programming language.

At a human level, the value of choice means each individual human
gets to choose what programming language to work in, or whether
to become a programmer at all. If you’re working at a company or
in any other sort of group project, that choice becomes a group
choice, and your human right to choice involves the choice of
whether to leave the group. If your boss makes you program in Rust
and you don’t like it, that is a threat to the human value of choice,
but one outside of the scope of the design of Rust.

But within a programming language, features are always curated. It is the
programming language designers’ choice of what features to include. Others
can choose different features for their programming languages, or even make
their own programming language that’s just like Rust but offers inheritance
to its users.

At this point, I begin to suspect that my critics simply value different
things in a programming language than Rust does. If choice is an important
value to your use case, as is valid if you’re a hobbyist programmer
programming to try to express yourself and have fun, then perhaps Rust
just isn’t for you. Perhaps you should use something more like Perl,
which offers tons of choices, or Python, which ironically doesn’t
impose “one true way” when it comes to paradigm, or an OOP language,
if you like specifically getting to choose between composition
and inheritance.

I usually don’t like using the argument “if you don’t like X, then feel free
to use something else.” But I do think it’s an appropriate response to a
complaint that X doesn’t offer choice for its own sake, assuming that X has
a valid reason not to offer that choice (which X often but not always does).
The choice still exists, at a different level, and I’d feel remiss if I
didn’t point that out.

In the case of inheritance, I would personally rather have people who like
it work in other programming languages. I’m glad that other programming
languages exist, to explore other parts of the programming language design
space, and to provide tools other than the tools Rust provides. But I
like Rust how it is, without pressure to make it more like all the
many OOP languages that offer inheritance, which I am exercising my
right of choice to avoid using whenever I practically can.

Subscribe
=========

Find out via e-mail when I make new posts!
You can also use [RSS](/index.xml) ([RSS for technical posts only](/computers/index.xml)) to subscribe!

Comments
========

If you want to send me something privately and anonymously, you can use
my [admonymous](https://www.admonymous.co/thecodedmessage) to admonish (or praise) me
anonymously.

[comments powered by Disqus](https://disqus.com)
