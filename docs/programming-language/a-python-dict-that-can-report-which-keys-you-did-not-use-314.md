---
id: 314
url: https://www.peterbe.com/plog/a-python-dict-that-can-report-which-keys-you-did-not-use
title: A Python dict that can report which keys you did not use - Peterbe.com
domain: www.peterbe.com
source_date: '2025-07-30'
tags:
- python
- tutorial
summary: This blog post introduces a custom Python `TrackingDict` class that extends
  the standard dictionary to monitor which keys are accessed and which are never used.
  This is useful for ensuring comprehensive unit test coverage and verifying that
  all retrieved data from databases is actually utilized in reports. The author provides
  both a basic implementation and an updated typed version contributed by a commenter,
  along with discussions about potential enhancements like supporting the `.get()`
  method and tracking mutations.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# A Python dict that can report which keys you did not use - Peterbe.com

A Python dict that can report which keys you did not use
========================================================

**Thursday, Jun 12, 2025**  
13 comments [Python](/oc-Python)

This can come in handy if you're working with large Python objects and you want to be certain that you're either unit testing everything you retrieve or certain that all the data you draw from a database is actually used in a report.  
For example, you might have a `SELECT fieldX, fieldY, fieldZ FROM ...` SQL query, but in the report you only use `fieldX, fieldY` in your CSV export.

```
class TrackingDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._accessed_keys = set()

    def __getitem__(self, key):
        self._accessed_keys.add(key)
        return super().__getitem__(key)

    @property
    def accessed_keys(self):
        return self._accessed_keys

    @property
    def never_accessed_keys(self):
        return set(self.keys()) - self._accessed_keys
```

Example use case:

```
user = {
    "name": "John Doe",
    "age": 30,
    "email": "jd@example.com",
}
user = TrackingDict(user)
assert user["name"] == "John Doe"

print("Accessed keys:", user.accessed_keys)
print("Never accessed keys:", user.never_accessed_keys)
```

This will print

```
Accessed keys: {'name'}
Never accessed keys: {'email', 'age'}
```

This can be useful if you have, for example, a `pytest` test that checks all the values of a dict object and you want to be sure that you're testing everything. For example:

```
assert not user.never_accessed_keys, f"You never checked {user.never_accessed_keys}"
```

**UPDATE (June 16)**

Here's a **typed** version, by commenter **Michael Cook**:

```
from typing import TypeVar, Any

K = TypeVar('K')
V = TypeVar('V')

class TrackingDict(dict[K, V]):
    """
    A `dict` that keeps track of which keys are accessed.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._accessed_keys: set[K] = set()

    def __getitem__(self, key: K) -> V:
        self._accessed_keys.add(key)
        return super().__getitem__(key)

    @property
    def accessed_keys(self) -> set[K]:
        return self._accessed_keys

    @property
    def never_accessed_keys(self) -> set[K]:
        return set(self.keys()) - self._accessed_keys
```

[Comments](#comments)
---------------------

[Post your own comment](#commentsform)

**Michael Cook** [June 13, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c264bdc) Reply

What would it look like with type hints?

**Peter Bengtsson** [June 13, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c3806f7) Reply

What do you think it cutoff look like?   
If you can make a version that you think will work, we can update the blog post.

**Peter Bengtsson** [July 8, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/cd65798) Reply

\*could  
(Not “cutoff”)

**Michael Cook** [June 14, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c2d6c27) Reply

How about this?  
  
from typing import TypeVar, Any  
  
K = TypeVar('K')  
V = TypeVar('V')  
  
class TrackingDict(dict[K, V]):  
    """  
    A `dict` that keeps track of which keys are accessed.  
    """  
  
    def \_\_init\_\_(self, \*args: Any, \*\*kwargs: Any) -> None:  
        super().\_\_init\_\_(\*args, \*\*kwargs)  
        self.\_accessed\_keys: set[K] = set()  
  
    def \_\_getitem\_\_(self, key: K) -> V:  
        self.\_accessed\_keys.add(key)  
        return super().\_\_getitem\_\_(key)  
  
    @property  
    def accessed\_keys(self) -> set[K]:  
        return self.\_accessed\_keys  
  
    @property  
    def never\_accessed\_keys(self) -> set[K]:  
        return set(self.keys()) - self.\_accessed\_keys

**Peter Bengtsson** [June 16, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c812562) Reply

Blog post updated, thanks to you! Thanks!

**mataha** [July 30, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c2423ae) Reply

TypeVars shouldn't be necessary, you can do just:  
  
from typing import TypeVar, Any  
  
class TrackingDict[K, V](dict[K, V]):  
    ...

**mcfur** [June 18, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/cd29df1) Reply

Cursor effects are annoying. I would discourage their use.

**Terry Spotts** [June 18, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c3bf32c) Reply

Interesting concept! I'm experimenting with this have and have noticed a few potential issues. Currently TrackingDict doesn't respond to the .get() method, an easy fix there might be inheriting from UserDict or refactoring to implement a MutableMapping? Another thing I noticed is that key lookup misses also get added to the \_accessed\_keys set. ex: a lookup to user["address"] wrapped in a try/except KeyError. This might be the desired behavior though?

**Peter Bengtsson** [June 19, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/cdde695) Reply

That's great points! The origin place where I wanted and needed this was only using `\_\_getitem\_\_` so I didn't think of `.get()`.

**Rene Nejsum** [July 30, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c3e81bd) Reply

I once made something like this, but also had an age on keys, so I could get a warning on old unused keys...

**lupl** [July 31, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c72d570) Reply

It would be better to subclass `collections.UserDict` for that.

**iloveitaly** [July 31, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/c2b8ece) Reply

Would be great to have this for pydantic! I'd love to track not just accessed items, but items that are mutated.

**rodrigo** [August 1, 2025](/plog/a-python-dict-that-can-report-which-keys-you-did-not-use/comment/cc5265a) Reply

A immutable Pydantic version (really immutable, with persistent data structures) would get me in love.

[Related posts](#related-posts)
-------------------------------

Previous:
:   [Set up iTerm to delete whole words on Option-Backspace](/plog/iterm-to-delete-whole-words-option-backspace) May 13, 2025 [macOS](/oc-macOS)

Next:
:   [Video to Screenshots app](/plog/video-to-screenshots-app) June 21, 2025 [React](/oc-React), [JavaScript](/oc-JavaScript), [Bun](/oc-Bun)

Related by category:
:   [Using AI to rewrite blog post comments](/plog/using-ai-to-rewrite-blog-post-comments) November 12, 2025 [Python](/oc-Python)
:   [Combining Django signals with in-memory LRU cache](/plog/combining-django-signals-with-in-memory-lru-cache) August 9, 2025 [Python](/oc-Python)
:   [Comparison of speed between gpt-5, gpt-5-mini, and gpt-5-nano](/plog/comparison-of-speed-between-gpt-5-mini-nano) December 15, 2025 [Python](/oc-Python)
:   [Autocomplete using PostgreSQL instead of Elasticsearch](/plog/autocomplete-using-postgresql-instead-of-elasticsearch) December 18, 2025 [Python](/oc-Python)

Related by keyword:
:   [Be careful with using dict() to create a copy](/plog/be-careful-with-using-dict-to-create-a-copy) September 9, 2015 [Python](/oc-Python)
:   [When to \_\_deepcopy\_\_ classes in Python](/plog/must__deepcopy__) March 14, 2012 [Python](/oc-Python)
:   [SmartDict - a smart 'dict' wrapper](/plog/SmartDict)  July 14, 2005 [Python](/oc-Python)

[Go to top of the page](#top)
