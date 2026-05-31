---
id: 28
url: https://www.thecodedmessage.com/posts/oop-3-inheritance/
title: 'Rust Is Beyond Object-Oriented, Part 3: Inheritance :: The Coded Message'
domain: www.thecodedmessage.com
source_date: '2026-01-07'
tags:
- rust
- tutorial
summary: This article argues that inheritance, one of the three traditional pillars
  of Object-Oriented Programming, is fundamentally flawed and unnecessary in Rust.
  The author clarifies that he opposes inheritance with shared fields (not interface
  implementation), explaining that "is a" inheritance is merely syntactic sugar for
  "has a" composition—making parent class fields implicit rather than explicit. The
  piece advocates for Rust's approach of using traits for polymorphism and explicit
  struct composition instead of inheritance, which provides clearer, more maintainable
  code.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Rust Is Beyond Object-Oriented, Part 3: Inheritance :: The Coded Message

[Rust Is Beyond Object-Oriented, Part 3: Inheritance](https://www.thecodedmessage.com/posts/oop-3-inheritance/)
===============================================================================================================

2023-12-07
:: Jimmy Hartzell

#[programming](https://www.thecodedmessage.com/tags/programming/) 
#[computers](https://www.thecodedmessage.com/tags/computers/) 
#[Rust](https://www.thecodedmessage.com/tags/rust/) 
#[OOP](https://www.thecodedmessage.com/tags/oop/) 
#[Beyond OOP](https://www.thecodedmessage.com/tags/beyond-oop/) 

In this next[1](#fn:1) post of my series explaining how Rust is better
off [without Object-Oriented Programming](/tags/beyond-oop/), I discuss
the last and (in my opinion) the weirdest of OOP’s 3 traditional pillars.

It’s not [encapsulation](/posts/oop-1-encapsulation/), a great idea which
exists in some form in every modern programming language, just OOP does
it oddly. It’s not [polymorphism](/posts/oop-2-polymorphism/), also a
great idea that OOP puts too many restrictions on, and that Rust
borrows a better design for from Haskell (with syntax from C++).

No, it’s that third pillar, inheritance, that I am discussing today, that
concept that only shows up in OOP circles, causing no end of problems
for your code. Unlike encapsulation and polymorphism, Rust does not
have any direct analogue.

> **Side note:** In this series in general, but especially in this post,
> I am primarily discussing static OOP languages, like C++ and Java,
> where interfaces have to be explicit and where classes correspond to
> different static types. Much of what I write would have to be adapted
> to apply to more dynamic “duck-typing” styles of OOP like
> in Python or JavaScript (or Smalltalk), and won’t apply as directly.
> This series is about why Rust isn’t OOP, and Rust is closer to C++ or
> Java than to a dynamic language, so this bias makes sense in context.

Why do people like inheritance?[#](#why-do-people-like-inheritance)
===================================================================

I can see why inheritance is so compelling. The entire system
of education encourages us to categorize things into neat little
hierarchies. Rectangles are a type of shape, and squares are a type of
rectangle. Humans are a type of animal, and men and women are types of
humans. Inheritance allows us to take this “X is a Y” and express it to
a computer.

This “is a” relationship is seen as intuitive. As the entire point of OOP
is to make programming more intuitive, more like reasoning about the
real world, inheritance is a perfect match for it. Just like we reason
about the real world with categories and subcategories, we can reason
about the world of our program in a similar way.

And this allows us to feel smart when we read introductions to inheritance
in various books on OOP programming. We see the `Tiger` class inherit
from the `Animal` class, or the `Rectangle` class inherit from the
`Shape` class.

We get so excited by the abstract principle of “is a” that we don’t even
notice that the examples have nothing to do with programming. We don’t
write code about shapes or animals. And even a drawing program or a zoo
inventory app wouldn’t use inheritance like this! If inheritance was so
useful as to be a pillar of OOP, why are there so few beginner examples
that involve things programs actually do?

What do I mean by inheritance?[#](#what-do-i-mean-by-inheritance)
=================================================================

First, let me clarify what I mean by inheritance, or rather what I don’t
mean.

I don’t mean every subtype-supertype relationship, where all values
of one type are also included in another, broader type. Subtyping
shows up in Rust all the time, particularly when it comes to
[lifetimes](https://doc.rust-lang.org/nomicon/subtyping.html).

I also don’t mean the version of inheritance that only involves
implementing an interface. In C++, you implement dynamic interfaces
through inheritance as a mechanism, even if the “superclass” is just
a list of methods. In Java, inheritance and interface implementation
are separate mechanisms. I am not talking about interface implementation
as inheritance, even though it is technically considered the same
feature in C++:

```
// This class has no fields, only virtual methods.
//
// In Java, we would call this an interface. In Rust, we would
// call this a trait.
class Shape {
public:
    virtual void draw(Surface &surface) const = 0;
};

// This is considered inheritance in C++. The Java equivalent
// would use `implements` instead of `extends`. And you could still
// do this in Rust with a trait.
class Square : public Shape {
    int size;
    int x;
    int y;
public:
    void draw(Surface &surface) const override;
};
```

I am only opposed to the type of inheritance that is still called
inheritance in Java. Having a type implement an interface (a *trait*
in Rust) is perfectly legitimate and still allowed in Rust, as is
casting a reference to a value to a generic, “dynamic” value based on
that trait or interface:

```
trait Shape {
    fn draw(&self, surface: &mut Surface);
}

struct Square {
    size: u32,
    x: u32,
    y: u32,
}

impl Shape for Square {
    fn draw(&self, surface: &mut Surface) {
    }
}

// Assume square is Square, surface is Surface
let shape: &dyn Shape = &square;
shape.draw(&mut surface);
```

`Shape`, in this context, is a pure interface. It is only a structured
form of polymorphism, not inheritance per se. Very importantly, `Shape` has
no fields. It is defined based solely on what you can do with it. And
accordingly, the “is a” language makes sense for interface implementation:
`Square` is a `Shape`. A `Shape` has no state, though, just methods, just
behaviors.

But some parent classes have fields. And that’s when inheritance really
starts to have problems: when the “parent” class has fields. It is at
this point that inheritance starts to seem really weird.

What does inheritance actually do?[#](#what-does-inheritance-actually-do)
=========================================================================

In my article on [encapsulation](/posts/oop-1-encapsulation), I discussed
how a class is secretly two things with the same name, entangled and
conflated:

* A **record type** (or what Rust would call a `struct`), that is, a type
  whose values consist of a number of fields with fixed names and types
* A **module** (a collection of code with enforced encapsulation boundaries),
  containing that record type and a collection of functions (called “methods”)
  for interacting with it

Inheritance does something different with each of these concepts.
To start out, let’s discuss what it does to the record type.
We’ll continue using shapes, a classic example for discussing
object-oriented features. A circle is a shape, so we can use inheritance
here:

```
class Shape {
public:
    Color color;
};

class Point {
public:
    int x;
    int y;
};

class Circle : public Shape {
public:
    Point center;
    int radius;
};
```

So, what does this mean for `Circle`? Well, it means that all the fields
of `Shape` (namely, `color`) are also fields of `Circle`. Therefore,
references to `Circle` can be made into references to `Shape`, as everything
you can do with a shape, you can do with a circle, like set the color,
or get the color:

```
Circle circle;
Shape &shape = circle;
shape.color = Color::Blue;
assert(circle.color == Color::Blue);
```

The thing is, we already have a mechanism of taking all the fields of
struct A and putting it in struct B: by putting a field of type A into
struct B! Instead of inheritance’s “is a,” we can accomplish the same
thing with having a field, or “has a.” In our example, we can do the
exact same thing with `Point` that we did with `Shape` – it just
involves being a little more explicit about what’s going on:

```
Circle circle;
Point &point = circle.center;
point.x = 3;
assert(circle.center.x == 3);
```

So, what does inheritance do to the classes from the **record type**
perspective? It makes the parent class a field of the child class,
just a field with no name. By writing:

```
class Circle : public Shape {
    // ...
```

… from a record type perspective, we were writing syntactic sugar for:

```
class Circle {
public:
    Shape shape;
    // ...
```

And when we wrote:

```
Shape &shape = circle;
```

That was translated into something like:

```
Shape &shape = circle.shape;
```

“Is a,” from a record type point of view, is just syntactic sugar for
“has a.” If you want to do something similar in Rust, just make a has-a
relationship, rather than creating an implicit field with no name.
Rust doesn’t like implicit nameless things anyway.

This will also save on arguing about whether two types have an “is a”
or a “has a” relationship. I regret all the time I’ve spent splitting hairs
about that distinction, when really, it’s just a matter of whether we want
a field to be implicit or not.

OK, so that covers what inheritance does to the record types, but
what about the rest of the class, the module? What happens to
the methods?

Well, for non-virtual methods, it’s also straight-forward. Instead of
doing inheritance, you can still just use has-a instead, and do a field
access. Instead of calling, say, `circle.get_color()`, we could always
call `circle.shape.get_color()`.

So far, with the fields and non-virtual methods, inheritance just
seems a bit weird and overrated. Like, we don’t see any reason yet
why a programming language would want to support it, when just having
a field of a superclass type does everything. But on the other hand,
some people like implicit fields and convenient short-hands, so there’s
not much of a downside either.

Inheritance without virtual methods may seem harmless, but it doesn’t
have much to do with the concept of “is a.” Technically, you can use a
field access as an implicit conversion, and think of it as a subtyping
relationship, but it doesn’t actually correspond to how the world
works. Even in the world of shapes, it doesn’t make sense: if a square
is a rectangle, how come it has less state than a rectangle, with only
one field for side length instead of two for width and height?

But we’ve not yet talked about virtual methods. When we do, you will
see why I think inheritance is not just an unnecessary feature, but an
ill-conceived anti-feature.

But what about the virtual methods?[#](#but-what-about-the-virtual-methods)
===========================================================================

So, earlier we discussed a class as being two things, a record type (with
fields) and a module (with methods and visibility restrictions). But
once we consider virtual methods, a class is actually three things with
the same name:

* A **record type**: each object has the fields
* A **module**: the type, trait, and other methods, are all in an encapsulated
  module
* A **trait** or **interface**: the virtual methods form an interface

> **Side note:** some programming languages consider all methods to be
> virtual for some reason. For these programming languages, everything I
> say still applies, but all methods are in the trait as they’re all virtual.
>
> Given that most methods aren’t self-consciously written with the intent
> to be virtual, making methods implicitly virtual seems like a good way
> to set the programmer up for surprise – that is, a horrible idea. But
> nevertheless having all virtual methods was for a long time considered
> the more ideological, more purely OOP way to do things, and so languages
> which strove to be purely OOP (like the original Java) did it.

Up until now, we have ignored this additional conflation,
this additional role that a class plays. In discussing
[encapsulation](/posts/oop-1-encapsulation/), we were discussing simply
how classes conflate the two distinct concepts of record types and
modules. In discussing [polymorphism](/posts/oop-2-polymorphism/), we
were assuming interfaces, and discussing how OOP’s version of interfaces
were constrained by insisting on a specific dynamic implementation. Only
now, now that we discuss inheritance, do we see that OOP not only
conflates record types and modules, but it also conflates record types
and interfaces.

When a class has virtual functions, that constitutes an interface,
implemented by dynamic polymorphism. But the only way you are allowed
to implement the interface is by inheriting from the class – that is,
by also having a (secret, unnamed, implicit) field of the record type.

See, as discussed above, inheriting from a class without virtual methods,
a class with just fields and regular methods, is no biggie. It’s just
a weird way of writing a has-a relationship that comes with some syntactic
sugar and automatic conversions – things I’m not a fan of and wouldn’t
put in my programming language, but not that bad.

Similarly, inheriting from a class without fields, a class with just
virtual methods (and perhaps regular methods, it turns out they barely
matter) is also no biggie. It has all the downsides of OOP-style
[polymorphism](/posts/oop-2-polymorphism/), but is fundamentally just a
way to indicate that you’re implementing an interface. In languages like
C++, inheritance is the mechanism by which you implement interfaces,
and in languages like Java, a methods-only class should probably be an
interface.

(To round out all the possibilities, I will mention that a class with
neither virtual methods nor fields is just a traditional module.)

But if you have both fields and virtual methods, then you have true
OOP-style inheritance, with all of its problems. You have an interface
that you can only implement if you inherit from the class. If you did
not intend this, perhaps because you are writing in a language like
Java where allowing inheritance is the default for classes and virtual
is the default for methods, you are setting yourself up for surprises
when someone inherits from your class and starts overriding methods.

If you did intend this, however, why? Why make implementing an interface
contingent on having certain state, on having a special unnamed field?
Why conflate these two fundamentally different concepts of containing
another record type’s state and having the new record implement an
interface?

There’s a number of problems with this conflation. Why would we assume
that in order to implement the methods, you need that state? What if that
state is represented differently, like on a disk, or over a network, or as
mathematical consequences by a formula? This conflation of implementation
and interface means that there is no sane way to implement proxy objects.

But more importantly than that, I’m not entirely sure what the upside
of this conflation is. It seems to make programming simpler in one
particular scenario, a scenario that I rarely see come up in real life,
a scenario that frankly seems like a code smell.

So what can we do instead?[#](#so-what-can-we-do-instead)
=========================================================

There is no inheritance in Rust. There are no fields in traits. There is
simply no way of saying that in order to implement a trait, your type
must have certain fields. Rather than conflate the concepts of record
types, modules, and traits in this God-concept of “class,” Rust keeps
these three concepts quite separate.

So if we have a design that requires inheritance (either because we think
in OOP or because we’re translating from an OOP programming language),
how would we represent that in Rust?

Well, the most straight-forward way would be to separate out the
different parts of the base class. Such a refactor would allow us to
express our design in Rust, as literally as possible. This is just meant
as a starting point, a proof of concept that our design can survive
in a language without inheritance. Alternative, often better ways of
replacing inheritance will follow subseqeuntly.

But here’s the straight-forward method: If the base class has just fields,
or just virtual methods, that’s easy: it becomes a `struct` or a `trait`,
respectively. Instead of inheriting from the class, a type would have that
`struct` as a field, or implement that `trait`. Actually, in this case,
the straight-forward method might just be perfect – you weren’t actually
using inheritance per se, just an odd syntax for a field or for implementing
an interface.

If it has both, we’d have to extract both a `struct` and a `trait`.
The fields would become a `struct`, of its own type. The interface of the
virtual methods would become a trait. The implementation of the virtual
methods would become the implementation of that trait for that `struct`,
or provided methods on the trait, depending on what makes more sense. Any
non-virtual methods would then become methods of the `struct` or provided
methods on the trait, again depending on what makes more sense in context.

At this point, it might make sense to consider some of the alternatives
that Rust provides to run-time polymorphism, as discussed in the
[polymorphism](/posts/oop-2-polymorphism/) post. Is a trait, especially
an OOP-style, object-safe trait, really what we want here? We’ve opened
up alternative designs now, and perhaps one of the alternatives makes
more sense.

Assuming we do want a trait, we can then go to all the “child” classes
and make them implement the trait. They also get a new field, perhaps
named `super`, to contain the parent. Their trait implementations would
then do a mix of implementing new methods, calling the same method on
`super`, and defaulting to the provided method.

And again, at this point it would be appropriate to consider whether we
even need the `super` field, or if perhaps we can get away with not
having it.

After this transformation, we have valid Rust code out of our
inheritance-based OOP-style design pattern. But there’s nothing requiring
us to use Rust to do it: you could do the same refactor of inheritance
structures in an OOP language.

If we were to do this transformation, we’ve paid a small cost of having
to potentially write `.super` (or whatever name we’ve given the parent
field) every once in a while, as well as writing trait implementations
that forward some method calls to the `super` field. In return, we’ve
deconflated the two very different concepts of interface and fields,
and opened ourselves up to more possibilities.

What should I actually do in Rust instead of inheritance?[#](#what-should-i-actually-do-in-rust-instead-of-inheritance)
=======================================================================================================================

But notice that in discussing this transformation, I encouraged you to
consider alternatives at two points. Rarely does this transformation make
sense literally, which is to say, rarely does a literal translation of
inheritance into Rust make sense. I find this quite telling, as it implies
to me that inheritance itself only rarely makes sense – and indeed, I
only tend to use inheritance in OOP languages where a framework requires
me to, or as an *ersatz*[2](#fn:2) replacement of sum types (i.e. Rust `enum`).

Here are some other patterns that replace inheritance hierarchies, that
you might find yourself considering instead:

* A regular `enum`. This actually covers most situations for me. Methods that
  would be overriden just do a `match` on the `enum` contents, and methods
  that would not, do not.
* `struct` types that contain a field with an `enum` types. The `enum`
  type represents all the different options, but the `struct` type contains
  the fields that are always the same.

```
struct MessageHeader {
    source: Address,
    destination: Address,
    seqnum: u32,
}

enum MessageBody {
    Ping(PingMessage),
    Pong(PongMessage),
    Request(RequestMessage),
    Response(ResponseMessage),
}

struct Message {
    header: MessageHeader,
    body: MessageBody,
}
```

Isn’t this so much nicer than putting `source`, `destination`, and
`seqnum` in the base class?

* `enum` variants that themselves contain `enum` types.

```
enum Message {
    Client(ClientMessage),
    Server(ServerMessage),
}

enum ClientMessage {
    Ping(PingMessage),
    Request(RequestMessage),
}

enum ServerMessage {
    Pong(PongMessage),
    Response(ResponseMessage),
    Error(ErrorMessage),
}
```

Now, if you want any message, your type is `Message`. If you know
for sure you have a client message, you can say `ClientMessage`.
Or if you know for sure it’s specifically a ping, you can say
`PingMessage`. It’s like a class hierarchy!

* A `struct` with a template-parameterized member to set a policy.

This is perhaps the most sophisticated replacement. Imagine you
have a class `SocketHandler` that handles reading from a socket.
Imagine it looks like this:

```
class SocketHandler {
    CircularBuffer socket_data;
public:
    void data_available(int fd);
protected:
    virtual size_t message_size(const char *data, size_t size) = 0;
    virtual void process_message(const char *data, size_t size) = 0;
};
```

How this is going to work is, `data_available` is going to grab more and
more data from the socket `fd` until `message_size` returns a non-zero
value. Then, it’ll call `process_message` with that data. During this
time, it’ll store the data in `socket_data`. All of that work is being
done by `data_available`, in the parent class, and you can imagine
that the socket dispatching library has a collection of these
socket handlers, something like `std::vector<std::unique_ptr<SocketHandler>>`
(or perhaps a map indexed by file descriptor).

The child class is responsible for overriding `message_size` and
`process_message` to actually interpret incoming data for a specific
protocol. You’d have a child class for each `SocketHandler` protocol,
and it would include internal state like sequence numbers, etc.

But rather than have these methods overriden by a child class, the
right way to do it is to have just those methods in a trait that a
`SocketHandler` has. You can see this when you extract the implicit
trait for `SocketHandler` for the Rust version:

```
trait SocketProtocol {
    fn message_size(&self, data: &[u8]) -> usize;
    fn process_message(&mut self, data: &[u8]) -> Result<()>;
}

struct SocketHandler<P: SocketProtocol> {
    buffer: CircularBuffer,
    protocol: P,
}

trait SocketHandlerTrait {
    fn data_available(&mut self, fd: u32) -> Result<()>;
}

impl<P: SocketProtocol> SocketHandlerTrait for SocketHandler<P> {
    fn data_available(&mut self, fd: u32) -> Result<()> {
        // Call `self.protocol.message_size/process_message`
    }
}
```

So, rather than each socket protocol inheriting from socket handler,
with its common state, the socket handler *has a* socket protocol, as
a policy. The `SocketProtocol` trait here can then be a compile-time,
static trait and `SocketHandlerTrait` can be the object-safe, dynamic
one, and the `std::vector<std::unique_ptr<SocketHandler>>` can
be replaced with `Vec<Box<dyn SocketHandlerTrait>>`.

This last refactor can be generalized. Instead of inheriting from
a base class to implement specific functionality, inject that
functionality using policies[3](#fn:3), and parameterize the `struct` with members that implement policy traits.
Then, if need be (and need might not be) write a separate dynamic trait
for the overall `struct`.

---

1. I know my [last post](/posts/oop-2-polymorphism) hasn’t been
   since February. I’ve been procrastinating this one for a long time,
   mostly because my life has been so gosh-darn busy, and also mostly
   because I don’t really instinctively remember what I (or anyone else)
   really liked about inheritance to begin with. [↩︎](#fnref:1)
2. Isn’t it weird that *ersatz* means replacement in German, but
   means mediocre as a replacement in English, so that “ersatz replacement”
   doesn’t mean “replacement replacement” but “mediocre replacement”?
   Or am I using the English word wrong? [↩︎](#fnref:2)
3. Policies are known in Gang of Four terminology as
   [strategies](https://en.wikipedia.org/wiki/Strategy_pattern). I’ve touched
   on the policy pattern in some [previous](/posts/endian_polymorphism/)
   [posts](/posts/multiparadigm/), and at some point should write a full
   post about it, as policies are my favorite thing. [↩︎](#fnref:3)

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
