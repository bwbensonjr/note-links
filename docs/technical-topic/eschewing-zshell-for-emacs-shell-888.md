---
id: 888
url: https://www.howardism.org/Technical/Emacs/eshell-fun.html
title: Eschewing Zshell for Emacs Shell
domain: www.howardism.org
source_date: '2026-02-28'
tags:
- tutorial
- common-lisp
summary: The author explains why they switched from traditional shells like Zshell
  and Bash to Emacs Eshell, highlighting that it integrates seamlessly with their
  editor-first workflow and offers unique advantages like built-in paging through
  Emacs and access to Emacs Lisp functions. Eshell combines shell and Lisp REPL capabilities,
  allowing users to write commands in a simplified syntax while leveraging Emacs features,
  and it includes powerful file selection through filters and modifiers inherited
  from Zshell. The article provides practical examples and customization tips to help
  users better understand and utilize Eshell's features, which are otherwise hampered
  by poor documentation.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Eschewing Zshell for Emacs Shell

I’ve done it. I’m now done with Zshell and Fish and Bash and all of
those guys…mostly. While they all have nice features, I find that
what drives my workflow is my editor. I start in Emacs, and then pop
over to shell for file manipulation and whatnot. I don’t start in the
shell and move around and *then* edit files.

Most Emacs users split the Emacs window and start a shell inside
Emacs, and pop over and back to that window. However, I’m finding that
Emacs’ `eshell` to be a better fit, for the more I use it, the better
I like it.

It’s problem is the lack of documentation…and a bit of misunderstanding.
Hence this essay. Before I get started, I would like to put a plug for
Mickey Petersen’s new book, [Mastering Emacs](https://www.masteringemacs.org), as he has an excellent
chapter on [mastering the eshell](https://www.masteringemacs.org/article/complete-guide-mastering-eshell) (which happens to be free).

Why?
----

A shell is a command-driven REPL. You type in a command and view the
results, type in another command…rinse and repeat. Fine until you type
something you expect to have a few lines, but if it responds with
hundreds of lines, you redo the command and pipe it through `less`.

But with EShell, you don’t need to bother with a pager, since if you
received too much information, hit `C-c C-p` which jumps you to the top
of the last command, and then `C-v` your way down. Or better yet, just
search for what you want. EShell means every command goes through the
*Emacs pager*.

To be even cooler, try the [Plan 9-like](http://www.masteringemacs.org/articles/2010/12/13/complete-guide-mastering-eshell/) approach using the *Eshell
smart display*, where you automatically begin at the top of the
command until you type a non-cursor-movement key.

The Emacs Shell has a few other advantages:

* Since it is written in Emacs Lisp, it has the same shell behavior
  between different operating systems.
* Along with access to all your scripts and programs, you also have
  access to Emacs functions … write your shell scripts in Lisp?
  Sure!
* Craft and extend your shell experience.

Eshell’s primary disadvantage shows when a program attempts to
control the terminal.[1](#fn.1)

While you might have *tried* EShell in the past, I doubt you inhaled
and noticed its *uniqueness*. Let’s level up…

Starting the Shell
------------------

Since my workflow is *driven from Emacs*, shells are temporary. I
pop out to a shell for a few commands, and then return to my work.
When I say *pop out to the shell*, I use the following function which
creates a buffer-specific window in the lower third portion and start
Eshell (which picks up that buffer’s directory).

```
(defun eshell-here ()
  "Opens up a new shell in the directory associated with the
current buffer's file. The eshell is renamed to match that
directory to make multiple eshell windows easier."
  (interactive)
  (let* ((parent (if (buffer-file-name)
                     (file-name-directory (buffer-file-name))
                   default-directory))
         (height (/ (window-total-height) 3))
         (name   (car (last (split-string parent "/" t)))))
    (split-window-vertically (- height))
    (other-window 1)
    (eshell "new")
    (rename-buffer (concat "*eshell: " name "*"))

    (insert (concat "ls"))
    (eshell-send-input)))

(global-set-key (kbd "C-!") 'eshell-here)
```

My function, `x` exits that shell and closes that window.

```
(defun eshell/x ()
  (insert "exit")
  (eshell-send-input)
  (delete-window))
```

Lisp REPL? Almost
-----------------

EShell is a Lisp REPL. The following works as you’d expect from such
a REPL:

```
$ (message "hello world")
"hello world"
```

However, in a shell, we care more for simplicity and speed of typing
that we do for semantic clearness, so we can, in this case, drop the
parens with the same results:

```
$ message "hello world"
"hello world"
```

Functions that begin with `eshell/` are available in Eshell without
the prefix, so calling the `eshell/echo` function makes the shell
experience less surprising:

```
$ echo "hello world"
"hello world"
```

If you put it in parens, you need to give it the full name:

```
$ (eshell/echo "hello world")
"hello world"
```

What about types? In a normal shell, everything is a string, but EShell
has a foot in both worlds:

```
$ echo hello world
("hello" "world")
```

A list of two strings. However, you can NOT attempt to pass that `echo`
to `car`… at least not directly:

```
$ car echo hello world
```

Returns an error, as does:

```
$ car (list hello world)
```

You see, once you bring in parens, you also bring in syntactic
specific-ness, so you would need to do this:

```
$ car (list "hello" "world")
```

EShell has a `listify` that converts its arguments to a list of strings:

```
$ listify hello world
("hello" "world")
```

But if you want to pass that data to something like `car`, you need to
surround it in curly braces, which is EShell’s way of saying, call some
shell-like-goodness, but return it like Lisp:

```
$ car { listify hello world }
hello
```

Upon a cursory review, it appears little difference between a simple
`list` and using `listify`, as under certain circumstance, they have the
same behavior:

```
$ listify hello world
("hello" "world")

$ list hello world
("hello" "world")

$ listify 1 2 3
(1 2 3)

$ list 1 2 3
(1 2 3)

$ list "hello world"
(#("hello world" 0 11
   (escaped t)))

$ listify "hello world"
(#("hello world" 0 11
   (escaped t)))
```

However, I got the following message from David, who said:

> The difference between `listify` and a ’list’ appears to be that
> calling `listify` on a list will not nest it in another list, e.g.
>
> ```
> (eshell/listify '(1 2 3)) ;; => (1 2 3), a list with 3 elements
> (list '(1 2 3)) ;; => ((1 2 3)), a list with one element
> ```
>
> Seems useful for a context where input may be a list, or not.

Variables
---------

As the documentation says,

> Since Eshell is just an Emacs REPL(1), it does not have its own scope,
> and simply stores variables the same you would in an Elisp program.

Running `printenv` only displays the environment variables:

```
$ setenv A "hello world"
$ getenv A
"hello world"
```

Use the `setq` to assign normal, Emacs variables:

```
$ setq B hello world
$ echo $B
hello
$ setq B "hello world"
$ echo $B
hello world
```

Preface with a `$`, you can access any Emacs variable:

```
$ echo $recentf-max-menu-items
25
```

Keep in mind that environment variables over-shadow Emacs variables:

```
$ setenv C hello
$ setq C goodbye
$ echo $C
hello
```

Finally, you can `source` Eshell variables from a file:

```
$ cat blah.eshell
setq FOO 42
setq BLING "bongy"

$ . blah.eshell
42
bongy

$ echo $FOO
42

$ echo $BLING
bongy
```

Loops
-----

Executing a series of commands on each matching file is a standard use
case for shells. While you *could* use a Lisp-like `dolist`, EShell
attempts to give you a similar shell-like syntax:

```
$ for file in *.org {
  echo "Upcasing: $file"
  mv $file $file(:U)
}
```

The `(:U)` converts the contents before it to upper case format. It
is a modifier, and I’ll babble on about this in the next section
(since this is one of Eshell’s best feature).

I find it interesting to note that `*.org` gives the `for` loop a list
to iterate over, but if there is more than one argument, a list is
created, as in:

```
$ for i in 1 2 3 4 { echo $i }
```

Passing more than one list *flattens* them into one list, so the
following works as you expect:

```
$ for file in emacs* zsh* { ... }
```

File Selection
--------------

If all you were doing was renaming a single file, or changing access
permissions on all files in a directory, you’d hardly need a flexible
shell, as *dired* or even Finder is sufficient for those tasks. A shell
comes in handy when selecting a subset of files based on a pattern, and
EShell really shines here, because of its filters (that it stole
from [Zshell’s modifiers](http://zsh.sourceforge.net/Doc/Release/Expansion.html)):

```
$ ls -al *.mp3(U)   # Show songs I own
```

The `*.mp3` part is just a normal globbing pattern we all know and
love, but the `(U)` part further filters the selection. In this
case limiting the selection to files you own.

The help for this feature is available in the shell, so type the
following:

```
$ eshell-display-predicate-help
$ eshell-display-modifier-help
```

While you may have seen the predicates before (since they are
similar to ZShell’s), the coolest part is that you can write some
ELisp code to add your own predicates and modifiers.

### File Filter Predicates

Here is a list of the filter predicates. These can be stacked, so
typing, `ls **/*(IW)` will display all the files in the current
directory (and sub-directories) that are writable by the group
owner or all accounts on the system.

|  |  |
| --- | --- |
| `/` | Directories (may accept `d` … gotta verify that) |
| `.` | Regular files |
| `*` | Executable files |
| `@` | Symlinks |
| `p` | named pipes |
| `s` | sockets |
| `U` | Owned by current UID |
| `u` | Owned by the given user account or UID, e.g. `(u'howard')` |
| `g` | Owned by the given group account or GID, e.g. `(g100)` |
| `r` | Readable by owner (A is readable by group) |
| `R` | Readable by World |
| `w` | Writable by owner (I is writable by group) |
| `W` | Writable by World |
| `x` | Executable by owner (E is executable by group) |
| `X` | Executable by world |
| `s` | `setuid` (for user) |
| `S` | `setgid` (for group) |
| `t` | Sticky bit |
| `%` | Other file types. |

These are fairly straight-forward. For example, list all the
directories:

```
ls -ld *(/)
```

Some symbols take options, like to list all files owned by the
`howard` account, specify the string with single quotes:

```
ls -ld *(u'howard')
```

The `%` requires a second parameter to specify the file type to
filter. These are taken from the `ls`, so `%c` will display char
devices. Here is the list if stole from the `ls` man page:

|  |  |
| --- | --- |
| `b` | Block special file |
| `c` | Character special file |
| `d` | Directory |
| `l` | Symbolic link |
| `s` | Socket link |
| `p` | FIFO |
| `-` | Regular file |

The options can be combined. For instance, list all symbolic links
owned by your account:

```
ls -l *(@U)
```

Or, list all symbolic links that you *don’t* own by prefixing the
`^` symbol:

```
ls -l *(@^U)
```

Gets more interesting with time and size filters which take
parameters. This is the cheat-sheet-like output from
`eshell-display-predicate-help`:

`a[Mwhms][+-](N|'FILE')`
:   access time ~~/-/= N
    months/weeks/hours/mins/secs (days if unspecified) if FILE
    specified, use as comparison basis; so a~~’file.c’ shows files
    accessed before `file.c` was last accessed.

`m[Mwhms][+-](N|'FILE')`
:   modification time…

`c[Mwhms][+-](N|'FILE')`
:   change time…

`L[kmp][+-]N`
:   file size +/-/= N Kb/Mb/blocks

The following examples should clarify how to use these:

To display all `org-mode` files in my directory that I’ve modified
since yesterday, I would type:

```
ls *.org(m-1)
```

Where the `m` is the modification time, the `-` means *less than*
and `1` refers to the day, since we didn’t specify any other time
period. To display the files we’ve modified over the last 8 hours,
we’d enter:

```
ls *.org(mh-8)
```

Compress everything which hasn’t been accessed in 30 days:

```
bzip2 -9v **/*(a+30)
```

The `**` symbol is recursive access to sub-directories.

Shell scripts (that end with a `.sh` and are executable (we specify
the `*` character first) that are 50k or larger (we use the `+` symbol):

```
ls ***/*.sh(*Lk+50)
```

To specify 50K, we first write `k` then `+` (to mean *or larger*)
and finally the size. The three stars, `***` is a recursive search
into sub-directories, but not to follow symbolic links.

### Modifiers

Modifiers are similar to filters mentioned above, except that begin
with a colon symbol, and they change the string, file or list that
precedes it. For instance, `:U` upper-cases a string or file name:

```
for f in *(:U) { echo $f }
```

Returns:

```
AB-TESTING-EXPERIMENTS.ORG
AB-TESTING-PRESENTATION.ORG
ACTIONSCRIPT-NOTES.ORG
ADIUM-PLUGINS-AND-EXTENSIONS.ORG
ALFRED.ORG
ANGULARJS-BOILERPLATE.ORG
ANGULARJS-MODULES.ORG
ANGULARJS-TESTING.ORG
APPLESCRIPT-RECIPES.ORG
APPLESCRIPT-SKYPE.ORG
...
```

The modifiers can also affect a variable. The following example
behaves the same as the previous example:

```
for f in * { echo $f(:U) }
```

Here is the complete list of modifiers for an individual string or
file name:

|  |  |
| --- | --- |
| `:L` | lowercase |
| `:U` | uppercase |
| `:C` | capitalize |
| `:h` | dirname |
| `:t` | basename |
| `:e` | file extension |
| `:r` | strip file extension |
| `:q` | escape special characters |
| `:S` | split string at any whitespace character |
| `:S/PAT/` | split string at each occurrence of `/PAT/` |
| `:E` | evaluate again |

Here is the list of modifiers for a list:

|  |  |
| --- | --- |
| `:o` | sort alphabetically |
| `:O` | reverse sort alphabetically |
| `:u` | unique list (typically used after `:o` or `:O`) |
| `:R` | reverse the list |
| `:j` | join list members, separated by a space |
| `:j/PAT/` | join list members, separated by `PAT` |
| `:i/PAT/` | exclude all members not matching `PAT` |
| `:x/PAT/` | exclude all members matching `PAT` |
| `:s/pat/match/` | substitute `PAT` with `MATCH` |
| `:g/pat/match/` | substitute `PAT` with `MATCH` for all occurrences |

To append the string, `-foobar`, to all files owned by you, *before*
the extension, you would type:

```
for F in *(U) { mv $F $F(:r)-foobar.$F(:e) }
```

### Custom Filter Predicates

As you know, the best part of Emacs is its ability to customize
everything…including your shell experience.

As [Mickey Petersen mentions](https://www.masteringemacs.org/article/complete-guide-mastering-eshell#adding-new-modifiers-and-predicates), we can create our own predicates to
filter out files. Wouldn’t it be nice if we could specify files
based on their internal Org `#+tags` entry. For instance, at
the top of my files, I add the following headers:

```
#+TITLE:  Alfred
#+AUTHOR: Howard Abrams
#+DATE:   [2013-05-15 Wed]
#+tags:    mac technical
```

I would like Eshell to be able to list files that end in `org`, but
with contents that include the `mac` tag, like:

```
ls *.org(T'mac')
```

If the filter used a single symbol, we would append a *tuple* to
`eshell-predicate-alist` that specifies the symbol and the
predicate function (that returns `true` or `nil`). Something like

```
(add-to-list 'eshell-predicate-alist '(?P . eshell-primary-file))
```

However, in our example, the `T` symbol takes the tag as a
parameter. In this case, we need a two-step process:

1. A function to parse the Eshell buffer to look for the parameter
   (and move the point past the parameter)
2. A predicate function that takes a file as a parameter

For the first step, we have our function *called* as it helps
*parse* the text at this time. Based on what it sees, it returns
the predicate function used to filter the files:

```
(add-to-list 'eshell-predicate-alist '(?T . (eshell-org-file-tags)))
```

I combine the two steps into a single function, as after the
function is done with Step 1, we will return a lambda expression
for Step 2.

The first step is to *parse* the text following the point looking
for the tag (surround in single quotes), and move the point forward
over the *option* for our filter function (notice the `goto-char`
to the end of the match).

```
(defun eshell-org-file-tags ()
  "Helps the eshell parse the text the point is currently on,
looking for parameters surrounded in single quotes. Returns a
function that takes a FILE and returns nil if the file given to
it doesn't contain the org-mode #+tags: entry specified."

  ;; Step 1. Parse the eshell buffer for our tag between quotes
  ;;         Make sure to move point to the end of the match:
  (if (looking-at "'\\([^)']+\\)'")
      (let* ((tag (match-string 1))
             (reg (concat "^#\\+tags:.*\\b" tag "\\b")))
        (goto-char (match-end 0))

        ;; Step 2. Return the predicate function:
        ;;         Careful when accessing the `reg' variable.
        `(lambda (file)
           (with-temp-buffer
             (insert-file-contents file)
             (re-search-forward ,reg nil t 1))))
    (error "The `T' predicate takes an org-mode tag value in single quotes.")))
```

The returned function loads the given file into a `temp-buffer`,
and search the contents for the regular expression. Returns `nil`
if the match wasn’t found (`false`), and anything else is
interpreted as `true`.

Now I can search for Homebrew commands without bringing up my beer
notes:

```
$ grep brew *.org(T'mac')
```

Since the `grep` is really the Emacs `grep` function, it brings the
results up in a buffer that I can click to load/edit.

Summary
-------

Of course the real beauty of EShell is the Emacs integration, for
instance, using `highlight-regexp` to colorize key words from expected
output, or piping the results to an Emacs buffer:

```
$ ls -al > #<buffer some-notes.org>
```

And then issue a `C-c |` on that results to create an `org-mode` table
you can continue to manipulate.

While the Eshell is baked into Emacs, and requires no customization,
I have [made a few improvements](https://github.com/howardabrams/dot-files/blob/master/emacs-eshell.org) that may be helpful to others.

Footnotes:
----------

[1](#fnr.1)

Programs like `top` wouldn’t work well in Eshell since it
these programs are still attempting to manipulate the world with
ancient VT100 control codes, and the Eshell mostly is expecting
standard textual output.

However, if you type `top`, `eshell` notices `top` on its *naughty
list* (actually, the list is called `eshell-visual-commands`), and
will farm it out to a special `comint` buffer.

In practice, I don’t notice this limitation, since most applications I
would like, I usually just use a similar program re-written in Emacs.
However, if you find an app that doesn’t work well in EShell, append
it to this list.
