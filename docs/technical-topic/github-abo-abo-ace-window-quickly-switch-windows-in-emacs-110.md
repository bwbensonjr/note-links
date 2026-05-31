---
id: 110
url: https://github.com/abo-abo/ace-window
title: 'GitHub - abo-abo/ace-window: Quickly switch windows in Emacs'
domain: github.com
source_date: '2025-12-07'
tags:
- github-repo
- cli-tool
summary: '**ace-window** is an Emacs package that provides fast and intuitive window
  switching by displaying labeled characters in each window''s top-left corner—users
  simply press the corresponding character to switch to that window. Unlike the standard
  `other-window` command (which requires multiple key presses for many windows) or
  `windmove` (which needs four key bindings), ace-window combines speed and predictability
  into a single key binding, typically `M-o`. Beyond basic window switching, the package
  offers additional actions like swapping, deleting, and creating windows, along with
  extensive customization options for keys, behavior, and appearance.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - abo-abo/ace-window: Quickly switch windows in Emacs

ace-window
==========

[![GNU ELPA](https://camo.githubusercontent.com/26588986534cc6cbe9b82d569554cc9f8f8e4b1155875cfe70b94d810c336daf/68747470733a2f2f656c70612e676e752e6f72672f7061636b616765732f6163652d77696e646f772e737667)](https://elpa.gnu.org/packages/ace-window.html)
[![MELPA](https://camo.githubusercontent.com/edfa4284dd9157d410de0117caf728bcfb7965053575ba32007dc33bcb8e6b42/68747470733a2f2f6d656c70612e6f72672f7061636b616765732f6163652d77696e646f772d62616467652e737667)](https://melpa.org/#/ace-window)
[![MELPA Stable](https://camo.githubusercontent.com/e9a36da4974a094c5cb712102f51944f26e4bd1041a81904561fc66df4a8267f/68747470733a2f2f737461626c652e6d656c70612e6f72672f7061636b616765732f6163652d77696e646f772d62616467652e737667)](https://stable.melpa.org/#/ace-window)

**GNU Emacs package for selecting a window to switch to**

What and why
------------

I'm sure you're aware of the `other-window` command. While it's great
for two windows, it quickly loses its value when there are more windows.
You need to call it many times, and since it's not easily predictable,
you have to check each time if you're in the window that you wanted.

Another approach is to use `windmove-left`, `windmove-up`, etc. These
are fast and predictable. Their disadvantage is that they need 4 key
bindings. The default ones are shift+arrows, which are hard to reach.

This package aims to take the speed and predictability of `windmove`
and pack it into a single key binding, similar to `other-window`.

Setup
-----

Just assign `ace-window` to a short key binding, as switching windows
is a common task. I suggest `M-o`, as it's short and not
bound to anything important in the default Emacs.

Usage
-----

When there are two windows, `ace-window` will call `other-window`
(unless `aw-dispatch-always` is set non-nil). If there are more, each
window will have the first character of its window label highlighted
at the upper left of the window. Pressing that character will either
switch to that window or filter to the next character needed to select
a specific window. Note that, unlike `ace-jump-mode`, the position of
point will not be changed, i.e. the same behavior as that of
`other-window`.

A special character defined by `aw-make-frame-char` (default = `z`)
means create a new frame and use its window as the target. The new
frame's location is set relative to the prior selected frame's location
and given by `aw-frame-offset`. The new frame's size is given by
`aw-frame-size`. See their documentation strings for more information.

The windows are ordered top-down, left-to-right. This means that if you
remember your window layouts, you can switch windows without even
looking at the leading char. For instance, the top left window will
always be `1` (or `a` if you use letters for window characters).

`ace-window` works across multiple frames, as you can see from the
[in-action gif](http://oremacs.com/download/ace-window.gif).

Swap and delete window
----------------------

* You can swap windows by calling `ace-window` with a prefix argument `C-u`.
* You can delete the selected window by calling `ace-window` with a double prefix argument, i.e. `C-u C-u`.

Change the action midway
------------------------

You can also start by calling `ace-window` and then decide to switch the action to `delete` or `swap` etc. By default the bindings are:

* `x` - delete window
* `m` - swap windows
* `M` - move window
* `c` - copy window
* `j` - select buffer
* `n` - select the previous window
* `u` - select buffer in the other window
* `c` - split window fairly, either vertically or horizontally
* `v` - split window vertically
* `b` - split window horizontally
* `o` - maximize current window
* `?` - show these command bindings

For proper operation, these keys *must not* be in `aw-keys`. Additionally,
if you want these keys to work with fewer than three windows, you need to
have `aw-dispatch-always` set to `t`.

Customization
-------------

Aside from binding `ace-window`:

```
(global-set-key (kbd "M-o") 'ace-window)
```

the following customizations are available:

### `aw-keys`

`aw-keys` - the list of initial characters used in window labels:

```
(setq aw-keys '(?a ?s ?d ?f ?g ?h ?j ?k ?l))
```

`aw-keys` are 0-9 by default, which is reasonable, but in the setup
above, the keys are on the home row.

### `aw-scope`

The default one is `global`, which means that `ace-window` will work
across frames. If you set this to `frame`, `ace-window` will offer you
only the windows of the current frame.

### `aw-background`

By default, `ace-window` temporarily sets a gray background and
removes color from available windows in order to make the
window-switching characters more visible. This is the behavior
inherited from `ace-jump-mode`.

This behavior might not be necessary, as you already know the locations
where to look, i.e. the top-left corners of each window.
So you can turn off the gray background with:

```
(setq aw-background nil)
```

### `aw-dispatch-always`

When non-nil, `ace-window` will issue a `read-char` even for one window.
This will make `ace-window` act differently from `other-window` for one
or two windows. This is useful to change the action midway and execute
an action other than the default *jump* action.
By default, this is set to `nil`.

### `aw-dispatch-alist`

This is the list of actions you can trigger from `ace-window` other than the
*jump* default. By default it is:

```
(defvar aw-dispatch-alist
  '((?x aw-delete-window "Delete Window")
	(?m aw-swap-window "Swap Windows")
	(?M aw-move-window "Move Window")
	(?c aw-copy-window "Copy Window")
	(?j aw-switch-buffer-in-window "Select Buffer")
	(?n aw-flip-window)
	(?u aw-switch-buffer-other-window "Switch Buffer Other Window")
	(?c aw-split-window-fair "Split Fair Window")
	(?v aw-split-window-vert "Split Vert Window")
	(?b aw-split-window-horz "Split Horz Window")
	(?o delete-other-windows "Delete Other Windows")
	(?? aw-show-dispatch-help))
  "List of actions for `aw-dispatch-default'.")
```

When using ace-window, if the action character is followed by a string,
then `ace-window` will be invoked again to select the target window for
the action. Otherwise, the current window is selected.

### `aw-minibuffer-flag`

When non-nil, also display `ace-window-mode` string in the minibuffer
when `ace-window` is active. This is useful when there are many
side-by-side windows and the `ace-window-mode` string is cutoff in the
minor mode area of the modeline.

### `aw-ignored-buffers`

List of buffers and major-modes to ignore when choosing a window from
the window list. Active only when `aw-ignore-on` is non-nil. Windows
displaying these buffers can still be chosen by typing their specific
labels.

### `aw-ignore-on`

When t, `ace-window` will ignore buffers and major-modes in
`aw-ignored-buffers`. Use M-0 `ace-window` to toggle this value.
:type 'boolean)

### `aw-ignore-current`

When t, `ace-window` will ignore `selected-window'.
