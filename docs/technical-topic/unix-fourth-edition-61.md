---
id: 61
url: http://squoze.net/UNIX/v4/README
title: UNIX Fourth Edition
domain: squoze.net
source_date: '2025-12-30'
tags:
- emulator
- tutorial
- devops
summary: This page provides a comprehensive guide to running UNIX Fourth Edition on
  a PDP-11 emulator using SIMH. It includes detailed instructions for installing the
  system from original tape files, booting the operating system, and performing various
  administrative tasks such as rebuilding the kernel, creating device files, and adding
  users. The guide also covers advanced topics like setting up rescue tapes, extending
  the filesystem to secondary disks, configuring serial lines for remote access, and
  installing additional software.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# UNIX Fourth Edition

[github](https://github.com/aap/) |
[mastodon](https://mastodon.sdf.org/@aap) |
[TX-0](http://tx-0.net) |
[PDP-1](http://pdp-1.net) |
[PDP-6/10](http://pdp-6.net) |
[PiDP-1](https://obsolescence.dev/pdp1.html) |
[p5.js](https://editor.p5js.org/aap/sketches) |

Related sites:
| [site map](/sitemap)

[squoze.net](/)
===============

* [› B/](/B/)
* [› C/](/C/)
* [› NB/](/NB/)
* [» *UNIX/*](/UNIX/)
* + [› 32v/](/UNIX/32v/)
  + [› V6 on rl01](/UNIX/V6_on_rl01)
  + [› bltj/](/UNIX/bltj/)
  + [› fs/](/UNIX/fs/)
  + [› restored/](/UNIX/restored/)
  + [› sysIII pdp11/](/UNIX/sysIII_pdp11/)
  + [› sysIII vax/](/UNIX/sysIII_vax/)
  + [› sysV pdp11/](/UNIX/sysV_pdp11/)
  + [› tools/](/UNIX/tools/)
  + [› v1man/](/UNIX/v1man/)
  + [› v2man/](/UNIX/v2man/)
  + [› v3man/](/UNIX/v3man/)
  + [» *v4/*](/UNIX/v4/)
  + - [» *README*](/UNIX/v4/README)
    - [› turnkey/](/UNIX/v4/turnkey/)
  + [› v4man/](/UNIX/v4man/)
  + [› v5/](/UNIX/v5/)
  + [› v5man/](/UNIX/v5man/)
  + [› v6/](/UNIX/v6/)
  + [› v6man/](/UNIX/v6man/)
  + [› v7/](/UNIX/v7/)
  + [› v8/](/UNIX/v8/)
* [› ling/](/ling/)
* [› math/](/math/)
* [› misc/](/misc/)
* [› plan 9/](/plan_9/)

UNIX Fourth Edition
===================

Here you can find the contents of
the [UNIX v4 tape](https://archive.org/details/utah_unix_v4_raw)
ready for bootstrapping, including a tar file of the filesystem.

* <unix_v4.tap> is the original tape file in simh format
* <bootstrap> are the first 38400 bytes of the tape
* <disk.rk> is the rest of the tape, an RK05 image
* <unix_v4.tar> is the filesystem extracted
* <install.ini> is an ini file for simh to install the system
* <boot.ini> is an ini file for simh to boot the system
* <sys.tp> some useful files for recompiling the kernel
* <aap.tp> some stuff of mine
* <nroff.tp> nroff from v6 to format the manual
* <man.tap> the manual

At first I extracted the disk image manually from the tape,
which resulted in `bootstrap` and `disk.rk`.
These are really nothing more than
the first 38400 bytes of the raw tape content and the rest.
Because `unix_v4.tap` is block based, one first has to strip it of its block sizes
to get the raw content.

Actually it's easier to just use the tape as it is and install a new system from it.

You can find the result of the following install procedure [here](turnkey).

Installing the system
---------------------

To install the system we just dump an RK05 disk image from tape to disk:

```
% pdp11 install.ini

[...]
        ; boot from TM0, now in mboot
=list
dldr
dtf
list
mboot
mcopy
rkf
tboot
uboot
=mcopy
'p' for rp; 'k' for rk
k
disk offset
0
tape offset
75
count
4000
=
```

Afterwards, we can just load `uboot` from tape to start UNIX:

```
=uboot
k
unix
mem = 64530

login: root
# ls
bin
dev
etc
lib
mnt
tmp
unix
usr
# sync
# ^E        ; end emulation
```

Running the system
------------------

To boot the system we don't need the tape.
Instead, we load `uboot` directly from the boot sector.
We specify `k` for RK05, then the filename `unix`.

```
% pdp11 boot.ini

[...]
        ; boot from RK0, now in uboot
k
unix
mem = 64530

login: root
#
```

Building a rescue tape
----------------------

We can also build a little rescue system to boot a kernel
from DECtape should anything go wrong.
We first have add a few device files for the tape drives.

To do this, attach a DECtape in simh, then create the files:

```
# ^E        ; end emulation 
Simulation stopped, PC: 002040 (MOV (SP)+,177776)
sim> at tc0 rescue.tp
sim> c
# chdir /dev
# /etc/mknod mt0 b 2 0
# /etc/mknod tap0 b 1 0
# /etc/mknod tap1 b 1 1
# /etc/mknod tap2 b 1 2
# /etc/mknod tap3 b 1 3
```

Now with our UNIX v4 tape attached (`att tm0 unix_v4.tap`) we
copy the files to disk, and then over to DECtape, the kernel as well:

```
# chdir /tmp
# mkdir resc
# chdir resc
# tp mt
dldr
dtf
list
mboot
mcopy
rkf
tboot
uboot
   8 entries
  12 used
  74 last
END
# tp mx
END
# ls
dldr
dtf
list
mboot
mcopy
rkf
tboot
uboot
# tp 0cr *
   8 entries
  12 used
 541 free
  36 last
END
# rm *
# chdir ..
# rmdir resc
# chdir /
# tp 0r unix
   9 entries
  66 used
 487 free
  90 last
END
# tp 0t
dldr
dtf
list
mboot
mcopy
rkf
tboot
uboot
unix
   9 entries
  66 used
 487 free
  90 last
END
#
```

Now check that it works:

```
# sync
# sync
# TC0: writing buffer to file: rescue.tp

Simulation stopped, PC: 002040 (MOV (SP)+,177776)
sim> b tc0
=unix
mem = 64530

login: root
#
```

Rebuilding the kernel and creating device files
-----------------------------------------------

Use the files provided by <sys.tp>:

```
sim> att tc1 sys.tp
sim> c
# chdir /usr/sys
# tp 1t
run
dmr/run
dmr/rk.c
ken/run
conf/conf.c
   5 entries
   9 used
 544 free
  33 last
END
```

Because the RK driver currently does not work correctly under emulation
when using multiple disks, the RK driver from v5 has been included here.
`conf.c` includes a line for the memory device.

Back up `rk.c` if you want to keep it, extract the files, and build the kernel:

```
# chdir /usr/sys/dmr
# mv rk.c rk.c.orig
# chdir ..
# rm -f conf/conf.c
# tp 1x
END
# sh run
alloc.c:
clock.c:
fio.c:
iget.c:
main.c:
nami.c:
prf.c:
rdwri.c:
sig.c:
60: Warning: assignment understood
61: Warning: assignment understood
slp.c:
subr.c:
sys1.c:
sys2.c:
sys3.c:
sys4.c:
sysent.c:
text.c:
trap.c:
bio.c:
cat.c:
dc.c:
dh.c:
dhdm.c:
dhfdm.c:
dn.c:
dp.c:
dv.c:
kl.c:
lp.c:
malloc.c:
mem.c:
partab.c:
pc.c:
pipe.c:
rf.c:
rk.c:
rp.c:
tc.c:
tm.c:
tty.c:
vs.c:
vt.c:
# mv a.out /unix
/unix: 0644 mode y
#
```

And reboot `unix`. We will now want to create a bunch of device files:

```
k
unix
mem = 64529

login: root
# chdir /dev
# rm -f null
# /etc/mknod mem c 1 0
# /etc/mknod kmem c 1 1
# /etc/mknod null c 1 2
# /etc/mknod rk0 b 0 0
# /etc/mknod rk1 b 0 1
# /etc/mknod rk2 b 0 2
# /etc/mknod rk3 b 0 3
#
```

The `/dev` directory should now look something like this:

```
# ls -l /dev
total 0
crw-rw-rw- 1 root    1,  1 Jun 12 20:05 kmem
crw-rw-rw- 1 root    1,  0 Jun 12 20:05 mem
brw-rw-rw- 1 root    2,  0 Jun 12 19:52 mt0
crw-rw-rw- 1 root    1,  2 Jun 12 20:05 null
brw-rw-rw- 1 root    0,  0 Jun 12 20:06 rk0
brw-rw-rw- 1 root    0,  1 Jun 12 20:06 rk1
brw-rw-rw- 1 root    0,  2 Jun 12 20:06 rk2
brw-rw-rw- 1 root    0,  3 Jun 12 20:06 rk3
brw-rw-rw- 1 root    1,  0 Jun 12 19:53 tap0
brw-rw-rw- 1 root    1,  1 Jun 12 19:51 tap1
brw-rw-rw- 1 root    1,  2 Jun 12 19:51 tap2
brw-rw-rw- 1 root    1,  3 Jun 12 19:51 tap3
crw--w--w- 1 root    0,  0 Jun 12 20:09 tty8
#
```

With `mem` in place `ps` will work. And we can use the disk devices
to extend our file system.

```
# ps a
 0     0 ???d??H??`?? ak??Z? ????? k?  ?  
 0     1 /etc/init  
 8     7 -  
 8    24 ps a   
 0     6 /etc/update  
#
```

Dumping the source code to a second disk
----------------------------------------

Now that we have a more reliable RK05 driver,
we can put the source code on a second disk.
To make this easy we use a scratch magtape:

```
sim> att tm0 src.tap
%SIM-INFO: TM0: creating new file
%SIM-INFO: TM0: Tape Image 'src.tap' scanned as SIMH format
sim> att rk1 src.rk
%SIM-INFO: RK1: Creating new file: src.rk
```

First we create a new file system, then we dump the source
directory to tape, and restore it on the new file system.

```
# /etc/mkfs /dev/rk1 4872
isize = 103
# /etc/mount /dev/rk1 /mnt
# chdir /usr/source
# tp mr *
 256 entries
1194 used
1256 last
END
# tp mt
s1/ac.c
s1/ar.s
s1/as11.s
s1/as12.s
s1/as13.s
s1/as14.s
s1/as15.s
[...]
# chdir /mnt
# mkdir s1 s2 s3 s4 s7
# chown bin *
# chmod 755 *
# tp mx
END
#
```

Now to delete the source from `/usr/source` and mount the new disk there instead.

```
# chdir /usr/source/s1
# rm -f [a-f]*
# rm -f *
# chdir ../s2
# rm -f *
# chdir ../s3
# rm -f *
# chdir ../s4
# rm -f [a-f]*
# rm -f *
# chdir ../s7
# rm -f *
# chdir ..
# rmdir *
# chdir /
# /etc/umount /dev/rk1
# /etc/mount /dev/rk1 /usr/source
```

To make this permanent:

```
# ed /etc/rc
70
$
/etc/update
i
/etc/mount /dev/rk1 /usr/source
.
w
102
q
#
```

Adding serial lines
-------------------

Make simh listen on some port (say, 4444):

```
sim> set dh en
sim> att dh 4444
```

On UNIX, we will create 8 teletype lines:

```
# chdir /dev
# /etc/mknod /dev/tty0 c 4 0
# /etc/mknod /dev/tty1 c 4 1
# /etc/mknod /dev/tty2 c 4 2
# /etc/mknod /dev/tty3 c 4 3
# /etc/mknod /dev/tty4 c 4 4
# /etc/mknod /dev/tty5 c 4 5
# /etc/mknod /dev/tty6 c 4 6
# /etc/mknod /dev/tty7 c 4 7
#
```

To make sure they work, connect to one via telnet and send it a message:

```
# echo hello >/dev/tty0
```

Now enable the 8 lines in `/etc/ttys`:

```
# ed /etc/ttys
56
1,8s/0/1/
w
56
q
#
```

If you now connect via telnet, you should be able to login.

Making new users
----------------

To create a new user `aap`, just pick a user ID and add
a new line to `/etc/paswd`.
Set a password with `passwd` if you like.

```
# ed /etc/passwd
30
$
bin::3:1::/bin:
a
aap::10:1::/usr/aap:
.
w
51
q
# mkdir /usr/aap
# chown aap /usr/aap
# ^D
login: aap
% pwd
../usr/aap
%
```

Installing new software
-----------------------

I have written some programs for multi-column output
and a better experience with underlined text.
If you like to use the, grab <aap.tp>
and mount it as, say `tc1`:

```
sim> att tc1 aap.tp
TC1: 16b format, buffering file in memory
sim> c
% tp 1t
mc.c
ul.c
p.c
   3 entries
   7 used
 546 free
  31 last
END
% tp 1x mc.c ul.c
END
% ls
mc.c
ul.c
% su
# cc mc.c
# mv a.out /usr/bin/mc
# cc ul.c
# mv a.out /usr/bin/ul
# ls /dev | mc
kmem   null   rk1    rk3    tap1   tap3   tty1   tty3   tty5   tty7   
mem    rk0    rk2    tap0   tap2   tty0   tty2   tty4   tty6   tty8   
mt0                                                                   
#
```

Nroff and the manual
--------------------

Unfortunately neither nroff nor the manual are included in the distribution,
so these come from elsewhere (TODO).
Get <nroff.tp> and <man.tap>.

First we build nroff. Unfortunately it's not quite behaving right at the moment
in that it resets the teletype to uppercase.
We can circumvent this for now with output redirection.

```
sim> at tc1 nroff.tp
TC1: 16b format, buffering file in memory

# chdir /usr/source/s7
# tp 1t
nroff1.s
nroff2.s
nroff3.s
nroff4.s
nroff5.s
nroff8.s
   6 entries
 113 used
 440 free
 137 last
END
# chown bin nroff*
# as nroff[1-5].s roff7.s nroff8.s
# ld -s -n a.out
# mv a.out /usr/bin/nroff
```

Then we install the manual and the `man` command:

```
sim> att rk2 man.rk
%SIM-INFO: RK2: Creating new file: man.rk
sim> att tm0 man.tap
%SIM-INFO: TM0: Tape Image 'man.tap' scanned as SIMH format
# /etc/mkfs /dev/rk2 4872
isize = 103
# chdir /usr
# mkdir man
# /etc/mount /dev/rk2 /usr/man
# chdir /usr/man
# mkdir man0 man1 man2 man3 man4 man5 man6 man7 man8 manx
# chown bin *
# chmod 664 *
# tp mx
END
# mv man /usr/bin/man
```

Now to test the whole thing:

```
# man cat | ul


CAT(I)                       1/15/73                       CAT(I)



NAME
     cat - concatenate and print

SYNOPSIS
     cat file ...

DESCRIPTION
     Cat reads each file in sequence and writes it on  the  stan-
     dard output.  Thus:

[...]
#
```

And make the mount permanent:

```
# ed /etc/rc
102
/mount/
/etc/mount /dev/rk1 /usr/source
a
/etc/mount /dev/rk2 /usr/man
.
w
131
q
#
```

Installing the B programming language
-------------------------------------

I have reconstructed the compiler and runtime system for B
and made it work on UNIX v4 and v5.
You can find the instructions [here](../../B/install)

Rebuilding the kernel (without sys.tp)
--------------------------------------

Put the following into `/usr/sys/run`:

```
rm -f low.o mch.o conf.o lib1 lib2

chdir ken
cc -c *.c
sh run
rm *.o

chdir ../dmr
cc -c *.c
sh run
rm *.o

chdir ..
cc -c conf/conf.c
mv conf/conf.o conf.o
as conf/low.s
mv a.out low.o
as conf/mch.s
mv a.out mch.o
ld -x low.o mch.o conf.o lib1 lib2
```

`/usr/sys/ken/run`:

```
ar r ../lib1 main.o
ar r ../lib1 alloc.o
ar r ../lib1 iget.o
ar r ../lib1 prf.o
ar r ../lib1 rdwri.o
ar r ../lib1 slp.o
ar r ../lib1 subr.o
ar r ../lib1 text.o
ar r ../lib1 trap.o
ar r ../lib1 sig.o
ar r ../lib1 sysent.o
ar r ../lib1 sys1.o
ar r ../lib1 sys2.o
ar r ../lib1 sys3.o
ar r ../lib1 sys4.o
ar r ../lib1 nami.o
ar r ../lib1 fio.o
ar r ../lib1 clock.o
```

`/usr/sys/dmr/run`:

```
ar r ../lib2 bio.o
ar r ../lib2 tty.o
ar r ../lib2 malloc.o
ar r ../lib2 pipe.o
ar r ../lib2 cat.o
ar r ../lib2 dc.o
ar r ../lib2 dn.o
ar r ../lib2 dc.o
ar r ../lib2 dn.o
ar r ../lib2 dp.o
ar r ../lib2 kl.o
ar r ../lib2 mem.o
ar r ../lib2 pc.o
ar r ../lib2 rf.o
ar r ../lib2 rk.o
ar r ../lib2 tc.o
ar r ../lib2 tm.o
ar r ../lib2 vs.o
ar r ../lib2 vt.o
ar r ../lib2 partab.o
ar r ../lib2 rp.o
ar r ../lib2 lp.o
ar r ../lib2 dhdm.o
ar r ../lib2 dh.o
ar r ../lib2 dhfdm.o
```

Then in `/usr/sys`:

```
# sh run
alloc.c:
clock.c:
fio.c:
iget.c:
main.c:
nami.c:
prf.c:
rdwri.c:
sig.c:
60: Warning: assignment understood
61: Warning: assignment understood
slp.c:
subr.c:
sys1.c:
sys2.c:
sys3.c:
sys4.c:
sysent.c:
text.c:
trap.c:
bio.c:
cat.c:
dc.c:
dh.c:
dhdm.c:
dhfdm.c:
dn.c:
dp.c:
dv.c:
kl.c:
lp.c:
malloc.c:
mem.c:
partab.c:
pc.c:
pipe.c:
rf.c:
rk.c:
rp.c:
tc.c:
tm.c:
tty.c:
vs.c:
vt.c:
#
```

Now install and boot the new kernel:

```
# mv a.out /nunix
# sync
# ^E
Simulation stopped, PC: 002040 (MOV (SP)+,177776)
sim> b rk
k
nunix
mem = 64529

login: root
#
```

TODO
----

There are a bunch of other things I would like to document
(or do in the first place):

* automatic installation (expect)
* try rp disk
* try rf swap (ps assumes rf0)

Reconstruction:

* get pre-v4 nsys kernel to work (buffer handling seems broken, i suspect synchronization bugs)
* get B restoration to work

[Powered by werc](http://werc.cat-v.org/)

[User Login](/_users/login)
