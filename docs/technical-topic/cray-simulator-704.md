---
id: 704
url: https://cray.modularcircuits.com/
title: Cray simulator
domain: cray.modularcircuits.com
source_date: '2026-01-13'
tags:
- emulator
- github-repo
- cli-tool
summary: This website provides access to an emulated Cray computer that users can
  log into via SSH or an in-browser client using the credentials crayusr/seymour.
  The simulator supports both command-line and graphical applications through X-forwarding,
  file transfers via SCP, and includes links to project documentation, source code
  on GitHub, and archived OS images for replication.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Cray simulator

Welcome to the Cray simulator
=============================

There are two ways to access the simulator. The first is through your regular SSH client:

`ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-dss -X crayusr@cray.modularcircuits.com -p 10022`

The other is to use the [in-browser SSH client](ssh)

In both cases the user name is **crayusr** and the password is **seymour**

The benefit of the first approach is that you can use X-forwarding and enjoy the graphical applications as well as the command line ones. If you have the patience, that is. Try 'xclock'

To transfer files from/to the machine, you can use SCP. Some special command line options are needed to make it work, so use the following incantantion as a template:

`scp -oKexAlgorithms=+diffie-hellman-group1-sha1 -oHostKeyAlgorithms=+ssh-dss -P 10022 -O <source> <destination>`

If you are interested in the background of the project, you can read up on it on my [blog](https://www.modularcircuits.com/blog/articles/the-cray-files/).

The source code of the project can be found on [GitHub](https://github.com/andrastantos/cray-sim).

You can also check out the [documentation library](cray_docs) I've collected over the years.

Finally, some nice person uploaded a couple of OS images to Archive.org which should allow you to replicate the simulator at home:

* <https://archive.org/details/cray-cd1>* <https://archive.org/details/cray-cd2>
