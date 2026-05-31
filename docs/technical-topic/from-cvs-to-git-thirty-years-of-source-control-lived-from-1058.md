---
id: 1058
url: https://evilgeniuslabs.ca/blog/from-cvs-to-git-thirty-years-of-source-control
title: From CVS to Git, thirty years of source control, lived from inside - EvilGeniusLabs.ca
domain: evilgeniuslabs.ca
source_date: '2026-05-04'
tags:
- github-repo
- tutorial
- devops
summary: The article traces thirty years of source control evolution from primitive
  methods like dated zip files in the 1990s through Git, which Linus Torvalds created
  in 2005 and remains the dominant standard today. It chronicles how each major system—from
  lock-based RCS, through CVS's concurrent editing model, to Microsoft's crash-prone
  Visual SourceSafe—solved specific problems of its era while introducing new ones.
  The author, who has used every major version control system since 1990, argues that
  Git's staying power for over two decades stems from its structural superiority,
  making it unlikely to be replaced despite being written in just ten days.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# From CVS to Git, thirty years of source control, lived from inside - EvilGeniusLabs.ca

0x07│
2026.04.28│
10 min read
│
**git · version-control · source-control · cvs · subversion · sourcesafe · history · programming · dvcs · github · opinion**
│
[history (v1)](/blog/from-cvs-to-git-thirty-years-of-source-control/history "View revision history")

From CVS to Git, thirty years of source control, lived from inside
==================================================================

In April 2005, Linus Torvalds wrote Git in ten days because BitKeeper revoked its free licence to the Linux kernel. Twenty-one years later, no successor has emerged. A practitioner's history of source control from someone who used every major system since 1990, and lost code in most of them.

![avatar](/uploads/avatars/74c3be59ff0d43f08a78943827988da2.png)

EvilGenius

[@EvilGenius](/u/EvilGenius)

In 1996 I was tracking source for a development shop, and the system was zip files. Filename was the project name plus the date. Backup was a tape that got rotated weekly. Branches were "copy the directory and rename it." Merging was Beyond Compare and a printout, and on a bad week it was Beyond Compare and an argument. We weren't unusual. Visual SourceSafe was the alternative for Microsoft shops, and Visual SourceSafe corrupted its own database often enough that "maintain offline backups of the SourceSafe repository" was a documented IT procedure, not a worst-case scenario.

Thirty years later I work in Git. Every shop I know works in Git. The thing called "modern source control" is the thing one Finnish kernel developer wrote in ten days in April 2005, and twenty-one years later there is no successor on the horizon. The reason is structural. Here's the path from there to here, lived from inside.

The pre-VCS era, what we did before formal version control existed
------------------------------------------------------------------

Practitioners who came up after 2010 may not know how bad it was. The before-picture is worth painting because it explains why the systems that followed look the way they do. Every choice in CVS, Visual SourceSafe, and eventually Git was a reaction to one of these failure modes.

There were zip files with date filenames. `project-2003-04-15.zip`. Endless archives in a backup directory, and on Monday morning the conversation was always "I think the working version is in last Tuesday's zip" because Friday's zip had a bug nobody could remember introducing. There were network shares with manual versioning: `FINAL`, `FINAL_v2`, `FINAL_FINAL`, `FINAL_REALLY`, `FINAL_USE_THIS_ONE`. The joke that's only a joke because everyone lived through it. Old VAX/VMS systems versioned every save at the file-system level: `MYFILE.TXT;3` was version three of the file, automatic, transparent, and a long-dead generation of VMS users still remember it fondly because nothing since has been quite so seamless. There was lock-by-whiteboard and lock-by-email ("I'm editing UTILS.BAS, don't touch it"), which was office practice in many shops well into the late 1990s. And every developer carried a small stack of dated 3.5-inch floppies with "the working version" on them, the personal version of the network share.

The argument for paying attention to any of this: before formal version control, every developer maintained their own ad-hoc system, and most of them were bad. The "I had a script that zipped my source tree every night" developer is the same human who later checked things into Git, just with worse tools and more anxiety.

The lock-based era, SCCS and RCS
--------------------------------

The first formal systems came out of Bell Labs and the early Unix research community.

SCCS, Source Code Control System, landed in 1972, written by Marc Rochkind. File-based, single-user, lock-based. Still ships with some Unixes today, usually as a footnote in the man pages. RCS, Revision Control System, followed in 1982 from Walter Tichy at Purdue, with better delta storage and per-file revision tracking, and it's still the substrate underneath several later systems. Both were lock-based. To edit a file under RCS you ran `co -l`, which marked the file as locked and let you edit it; everyone else was blocked until you ran `ci`. One file at a time. No notion of a *project* yet. The unit of versioning was the individual file.

What this era taught the rest of source control was the vocabulary. Deltas, meaning diffs between revisions stored efficiently. Check-out and check-in. History as a first-class concept. RCS's storage format, the `,v` files, became the on-disk substrate for CVS a few years later. The lock-based era was correct given its constraints (single workstation, no real network) and wrong for any larger team. The next thirty years of version control history is a sequence of attempts to lift those constraints.

CVS, concurrent edits, server-based, badly
------------------------------------------

The first system that scaled, and the one that dominated open source from roughly 1990 to 2005.

Dick Grune wrote the original CVS, Concurrent Versions System, in 1986. Brian Berliner took it over in 1989 and shipped what most people remember. CVS sat on top of RCS and used those `,v` files as its per-file storage backend, but it added the thing that mattered: concurrent edits. Multiple developers could check out and edit the same file, and CVS would merge their changes on commit. That single change killed the lock-based model for serious open-source work and introduced the concept of a *repository* as a first-class artifact, a thing you cloned, contributed to, and tagged.

What CVS didn't solve, and what made it eventually unbearable, was almost everything else. There were no atomic commits; a commit that touched five files committed each one separately, and if the network died halfway through, the repository was in an inconsistent state and someone had to reconcile it manually. Branches existed but creating one was slow, sometimes minutes for a large repository, and merging was manual and brittle. Renames were not tracked at all; moving a file meant deleting it and re-adding it, losing the entire history. Binary files were second-class because diffs assumed text. There was no directory versioning; you couldn't version *the structure* of the project, only the files in it. And the repository itself was a fragile pile of `,v` files on a server somewhere; backup was IT's problem, and if the server's disk failed, history was gone.

Anyone who used CVS for serious work in the 1995 to 2005 window has stories. The merge conflict on commit where half the files committed and half didn't, leaving the trunk in a state nobody could describe. The slow-branch problem, where the team avoided branching because it took five minutes to create one and an afternoon to merge it. The "someone deleted a directory and CVS lost its mind" class of bug. CVS dominated despite all of this because it was free, it was on every Unix, and there was no real alternative until 2000. Open-source projects ran on it because the alternative was nothing.

Visual SourceSafe, the parallel commercial track
------------------------------------------------

While the Unix world was working through CVS, the Microsoft world had its own track, and most VB6 and early-.NET developers actually lived in Visual SourceSafe.

SourceSafe started in 1992 at One Tree Software in Mountain View. Microsoft acquired the company in 1994 and re-released the product as Visual SourceSafe, bundled with Visual Studio, Visual Basic, and various Microsoft developer products through to roughly the mid-2000s. The model was lock-based pessimistic concurrency by default. Check out a file, edit it, check it back in. Other developers could see the file but not edit it during the lock. Multi-checkout was possible but dangerous because VSS's merge tooling was crude and most teams had a verbal rule against it. Microsoft picked the safer-feeling locking discipline where Unix went the other way, and made it the default for an entire generation of Windows developers.

The infamous part was the corruption. VSS stored its data in a custom file-database, `.dat` files in a shared network directory, and the format was fragile. Concurrent access, especially over slow or flaky network shares, could corrupt the database. "The VSS database is corrupt, run Analyze, restore from last night's backup if Analyze can't fix it" was a documented IT procedure in Microsoft shops, not a worst-case scenario. Everyone who used VSS in production has at least one corruption story, and the ones who don't are the ones who got out before they were due.

The mental tax was the other piece. Locking discipline meant developers couldn't work in parallel on overlapping code without coordinating verbally. "Hey, are you done with `frmMain.frm` yet?" was the daily nine-am standup question in shops I worked with through the late nineties. Branches existed but were rarely used because branching was slow and merging was painful, so the typical VSS shop maintained a single trunk and shipped from it.

VSS persisted despite all of this because it came with Visual Studio. It integrated cleanly with the Microsoft toolchain, it worked-ish for small teams on local networks, and the alternative was CVS (which Windows shops mostly didn't use) or no source control at all, which was the actual default for a depressing fraction of Microsoft-shop projects in the late nineties. Microsoft eventually replaced VSS with Team Foundation Server in 2005, which became Azure DevOps, and by the late 2000s VSS was deprecated. Most shops migrated to TFS, or once Git arrived and didn't suck, jumped straight to Git.

Subversion, "CVS done right"
----------------------------

The thing that should have won, and almost did, before Git arrived two years later.

CollabNet started Subversion in 2000, with the explicit pitch of "CVS done right." It became an Apache top-level project, and the first stable release, 1.0, shipped in February 2004. Designed by people who knew CVS's flaws and addressed them line by line.

What SVN fixed was substantial. Atomic commits, where multi-file commits succeed or fail as a whole and the repository is never left half-updated. Real branching, with cheap server-side copies, so branches and tags became first-class operations rather than afternoon-long procedures. Directory versioning, which meant renames were tracked and the project's structure was versioned alongside file contents. Binary files were first-class. The client-server protocol was WebDAV-based and played well with HTTP infrastructure, which mattered for shops that had to push source control through corporate proxies.

What SVN didn't fix was the fundamental centralized model. You could not commit without a network connection. The repository was still a single server. "Working offline" meant "reading-only", you could browse history but not record any new work, and the day the server was down was the day the whole team waited.

SVN almost won. From 2004 to 2008 it was the obvious choice for "better than CVS", and a great many projects migrated CVS to SVN with no awareness that the distributed-VCS earthquake was about to land like a truck. I used SVN in the mid-2000s and remember the relief of atomic commits the way you remember a good meal after a long flight. It just didn't last, because the next system did everything SVN did and removed the server constraint entirely.

April 2005, the month version control changed forever
-----------------------------------------------------

The story is genuinely good and most developers under 35 don't know it.

The setup was BitKeeper. Larry McVoy's BitKeeper was a proprietary distributed version control system, founded around 2000. The Linux kernel community used it from 2002 to 2005. Linus picked it because it was the only DVCS that could handle the kernel's scale and merge-heavy workflow, and McVoy provided a free-for-open-source-projects licence on the condition that nobody tried to reverse-engineer the protocol.

In April 2005 the licence blew up. Andrew Tridgell, the *Tridge* of Samba and rsync fame, had started writing a tool that talked to BitKeeper repositories. McVoy considered this a violation of the licence terms and revoked the free licence to the Linux kernel community. The kernel project, the largest collaborative software effort on Earth at that point, suddenly had no version control system.

Linus started writing Git on April 3, 2005. The first self-hosted commit landed on April 7. Within ten days he had something usable; within months it was tracking the Linux kernel. The design constraints came directly from his experience with BitKeeper and from his frustration with everything before it. Distributed, not centralized. Every clone is a full repository with full history, and there is no single point of failure. Fast enough to handle the kernel's scale, where every other system had buckled. A content-addressed object database, where every blob, tree, and commit is identified by its SHA-1 hash, which makes the repository structurally a Merkle tree and makes corruption detectable rather than silent. Cheap branching: branches are just pointers to commits, so creating one is an O(1) operation rather than the multi-minute procedure CVS made it. Three-way merge as the algorithmic default, not a manual reconciliation step.

Git wasn't alone in 2005. Mercurial (Hg) was started by Matt Mackall in April 2005, almost simultaneously with Git, and made different design choices: a simpler internal model, a more user-friendly CLI, and comparable performance. Bazaar (bzr) followed later in 2005, sponsored by Canonical and used for Ubuntu and Launchpad. Earlier DVCS projects, including Monotone, darcs, and GNU arch, informed the cohort but never reached mass adoption. The 2005 to 2010 adoption arc collapsed an entire genre of version-control design into one shape. The Linux kernel adopted Git immediately. Other open-source projects migrated from CVS and SVN to Git or Mercurial through 2006 to 2008. The community split between Git and Mercurial for a while; Git won, partly because of the Linux kernel halo effect, and mostly because of GitHub.

Git wasn't a slow evolution from previous systems. It was a clean break, written in two weeks, by a developer who had hit the wall of every prior model. The 2005 DVCS earthquake collapsed the design space into one shape that's still dominant.

GitHub, the platform that made Git the default
----------------------------------------------

Git the tool was Linus's. Git the cultural default was GitHub's.

Tom Preston-Werner, Chris Wanstrath, and PJ Hyett, joined later by Scott Chacon, launched GitHub in February 2008. The initial pitch was modest: a hosted Git server with a web UI. What GitHub actually delivered was the pull-request workflow. Forks, branches, diffs, review, merge: a collaboration pattern that Git supported in principle but GitHub made *visible*, *clickable*, and *social*. Repositories were public by default unless you paid, which made "show your work" the default for open-source contribution. Issues, wikis, releases were collaboration-adjacent features that turned GitHub from a Git host into a project-hosting platform. And as more projects landed on GitHub, contributing to open source became "have a GitHub account", and the network effects compounded.

Microsoft acquired GitHub in June 2018 for $7.5 billion. The structural fact is worth sitting with: the company that wrote Visual SourceSafe now owns the canonical home of Git. The acquisition has been net-positive for GitHub features and net-neutral for community trust. "Microsoft owns it" is a real fact developers track, not a crisis.

Competitors haven't displaced GitHub but they exist. GitLab, started in 2011, is self-hostable and a real competitor with a meaningful market position, particularly in enterprises and Europe. I host my own GitLab at gitlab.glyphdeck.org and have moved my personal projects there from GitHub. The alternative works, but I'd be lying if I said the gravitational pull of GitHub for collaboration didn't still matter. Bitbucket, Atlassian-owned, originally Mercurial-only, shifted to Git and has a smaller share now. Codeberg, Forgejo, and Gitea round out the community-driven end.

Without GitHub, Git would still have won technically, but it would have taken longer, and the "every developer has a GitHub profile" cultural default would not exist.

Git in 2026, what won, what didn't, what's next
-----------------------------------------------

Twenty years is forever in tech years, but not literally. The current state is worth a brief, honest read.

Git owns the field. GitHub, GitLab, Bitbucket, Codeberg, Gitea: every major code-hosting platform is Git-backed. Microsoft owns Git's biggest cultural surface through GitHub, which is a structural fact about the industry, notable but not necessarily problematic. Git itself has improved meaningfully since 2005. Git LFS for large files, partial clone, sparse checkout, a better submodule story through worktrees and subtrees, better rebase tooling, signed commits, and merge and diff algorithms that handle the corner cases the original Git tripped on. Git in 2026 is a better tool than Git in 2008.

Challengers worth knowing about exist, and none of them has displaced anything. Sapling came out of Meta, formerly an internal tool, with a Git-compatible backend and a different UX; it was open-sourced in 2022. Pijul takes a patch-theory approach with more mathematically rigorous merging, an active research project with a small community. Jujutsu (jj) is Martin von Zweigbergk's project at Google, started around 2023, Git-compatible underneath with a different command surface that handles things like in-progress changes and history rewriting more cleanly. All three are interesting. None is going to displace Git in the next decade.

What hasn't changed since 2005 is the fundamental DAG-of-commits model, the content-addressed object store, and the distributed clone-repo paradigm. Git's core data model is twenty-one years old, and there is no challenger on the horizon that would obsolete it.

The practitioner arc, what each system cost, what Git gave back
---------------------------------------------------------------

The personal-credential section, because the post is mostly worth what the experience under it is worth.

Zip-and-date, late 1990s consultancy era. My backup script was a tape drive, my "branch" was a renamed directory, and my recovery story was "go find the right zip from last week."

VSS, mid-to-late 1990s, the VB6 era. "The database is corrupt, restore from backup" is the phrase practically every Microsoft-shop developer of that era can repeat from muscle memory.

SVN, mid-2000s. Finally something that didn't lose data atomically, with a single point of failure I couldn't escape.

TFS and Azure DevOps, government and enterprise era. Finally something that didn't lose data at all, but you needed a corporate licence to use it and the workflow was built around a centralized server I couldn't take with me.

Git, from roughly 2010 onward. The day I ran `git init` and committed something locally, without a server, was the day everything else became obsolete.

And Git is not a panacea. On 2026-04-22, four days before this post was drafted, I lost roughly 344 lines of code across six files to a sloppy `git checkout HEAD --` on a file list that didn't include all the files I'd modified. The recovery cost significant time and the rebuilt code is plan-faithful but not byte-identical. The lesson there isn't "Git is bad." Git was correctly doing exactly what I told it to do. The lesson is "commit frequently and don't trust surgical destructive commands without backing up first," and that rule now lives in the global instructions I give my AI tooling, for a reason. Every system before Git took something from the developer. Git is the first one that mostly gives back. The remaining failure modes are user-error class, not platform-design class, and that's a category of progress worth being honest about.

Closing
-------

Git is twenty-one years old. The thing called "modern source control" is the thing one Finnish kernel developer wrote in ten days in April 2005, after BitKeeper revoked its licence to the Linux kernel community and forced his hand. Twenty-one years and a few hundred billion dollars of industry investment later, no successor has emerged. Pijul is interesting. Sapling is interesting. Jujutsu is interesting. None of them is going to replace Git in the next decade. The system you're using to push code in 2026 is the same system Linus wrote in two weeks during the largest licensing crisis in open-source history, and that is genuinely the way the world works.

Most days, I am still grateful.

//-EG\_

// comments
-----------

1 ENTRY

// sign in to comment

[Log in](/Identity/Account/Login?returnurl=%2Fblog%2Ffrom-cvs-to-git-thirty-years-of-source-control%23comments)
[Register](/Identity/Account/Register?returnurl=%2Fblog%2Ffrom-cvs-to-git-thirty-years-of-source-control%23comments)

1. You missed Perforce. The games industry, and many others then and now, did not. AlienBrain also did well for a while, especially in industries where the majority of contributing devs were not programmer/typists, but artists and sound designers, juggling many binaries that dwarfed coder texts in both counts and size.

   I appreciate that your focus is ‘source text’ but that’s a small if fiddly part of content management and version control in the development and maintenance of most interactive packages.

   // edit history
   1 previous version

   1. v1
      ·
      2026.05.12 01:40
      ·
      by Simon N Goodwin

      You missed Perforce. The games industry, and many others then and now, did not. AlienBrain also did well for a while, especially in industries where the majority of contributing devs were not programmer/typists, but artists and sound designers, contributing many binaries that dwarfed coder texts in both counts and size.

      I appreciate that your focus is ‘source text’ but that’s a small if fiddly part of content management and version control in the development and maintenance of most interactive packages.
