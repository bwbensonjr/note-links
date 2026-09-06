---
id: 1332
url: https://cloudinabottle.org/blog/launch-post
title: 'Cloud in a Bottle: making self-hosting accessible to everyone | Cloud in a
  Bottle'
domain: cloudinabottle.org
source_date: '2026-09-06'
tags:
- devops
- github-repo
- security
- cli-tool
summary: Cloud in a Bottle is an open-source personal cloud platform designed to make
  self-hosting accessible to non-technical users by offering containerized apps with
  unified authentication and a smartphone-like experience. The project addresses the
  problem that modern cloud software has become centralized and controlled by companies
  with misaligned incentives, whereas the open-source model thrived when individuals
  could host software themselves. The platform provides security through containerized
  sandboxing, integrated app experiences through shared APIs, and both self-hosted
  and managed versions, with plans to grow its curated app catalog to make personal
  cloud computing practical for everyday users.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Cloud in a Bottle: making self-hosting accessible to everyone | Cloud in a Bottle

TLDR: Cloud in a Bottle is your open-source personal cloud: containerized apps, unified auth, good UX. Self-hosting should feel like using a smartphone that serves webapps, not a sysadmin side job.

![screenshot of the dashboard](/blog/images/dashboard_screenshot.webp)

I'm frustrated with the state of the digital world. The software we use is so misaligned with our own incentives (intentionally addicting, loaded with ads, tracking you and selling your data, enshittifying). Software is easier than ever to make; how did we end up here? I think a big reason is the shift of software into the cloud. Software served from the cloud (think Google Docs vs Microsoft Word) delivers a great experience - no install, accessible on all your devices, immediate sharing/collaboration. But to serve something in the cloud costs money, and so just about everything on the modern web has a company behind it - open source authors naturally don't want to pay to serve their free software to the world. And those companies have a financial incentive fundamentally misaligned with our own.

In the pre-cloud days, open source worked - authors distributed their software, and everyone "hosted" it for themselves (i.e. ran it on their own PC). Nowadays, cloud software is centralized, with one instance of the software serving the world, and the costs borne by the creator. This is because individuals don't have an accessible way to put software into the cloud for themselves.

Self-hosting exists already, but it's niche and unapproachable. When I looked at the existing options, none of them felt right:

* [sandstorm.io](https://sandstorm.io/): very close in spirit ([their article](https://sandstorm.io/news/2014-07-21-open-source-web-apps-require-federated-hosting) from 2014 makes basically the same argument I'm making here), but unfortunately long abandoned. It also required significant changes to existing software to run on their platform.
* [nextcloud](https://nextcloud.com/): slow and unreliable, and more enterprise-targeted now
* [yunohost](https://yunohost.org/): apps run directly on the host, no sandboxing. one insecure app compromises the entire server.
* [coolify](https://coolify.io/): hosts containerized apps, but every app is an island with its own login and little integration with the host or other apps.

We created Cloud in a Bottle to take another stab at this. At the core, it's just an Ubuntu machine with a web server that hosts a dashboard and routes HTTP(s) requests to containerized apps. Apps are (rootless, hardened) containers, so it can run existing software with minimal changes - and in a reasonably secure sandbox. But beyond just hosting containers (like e.g. coolify), there are various opt-in platform features that apps can take advantage of to make the experience better. In a way, I want it to feel like your "cloud smartphone" - something that you own, where finding and installing great apps is trivial, and where the user experience is as good as the closed source products we're trying to replace. As a basic example, if you're logged into your instance, you're automatically logged into all your apps - no separate accounts in each app. And there's an interface to allow permissioned access to data and capabilities between different apps in your instance. More generally - think of all the different APIs that Android or iOS provide to enable apps to deliver a great, integrated experience (sensor access, notifications, health data sharing, etc). We've put a lot of time into thinking about the right analog of those APIs in the context of a personal cloud.

It's open source, self-hostable, zero telemetry, and aims to be as simple and "magic-free" as possible. We ([Imbue](https://imbue.com/), the company I work for) also offer a managed version, which I think is really important to making this widely accessible - and it gives us a straightforward business model to support the project. But the open-source/self-hosted path runs exactly the same code and will always be first-class.

We're launching now after building and testing it privately for 6+ months, now that the core platform is mostly complete and stable. I've been slowly moving my digital life into my own Bottle instance, and it's felt great. That said, there's a chicken and egg problem - without a broadly accessible way to self-host open source web software, the audience for such software is small, and the available software is limited. A big goal of ours is catalyzing the creation of more great open source web software - things we can recommend to friends and parents, not just other software nerds. Our [curated app catalog](https://cloudinabottle.org/apps) is one step in this direction - we aim to maintain a high bar, only adding things that actually deliver a great user experience, so it's pretty small right now. But we're adding things every week - and we hope to grow it faster with the help of the community. For now, early users will likely need a bit of technical familiarity (or a coding agent) to find/create/adapt the things you want to run on your instance (it's [really easy](https://cloudinabottle.org/docs/creating_an_app/overview.html)!). Over time, as the catalog gets deeper and we polish the experience further, we hope for it to become increasingly accessible to everyone.

Want to check it out?

* [Try a managed instance for free ($10 credit)](https://cloudinabottle.imbue.com/)
* [Self-host on a cloud VPS](https://cloudinabottle.org/docs/setup/cloud_instance.html)
* Install on your own hardware ([in a VM](https://cloudinabottle.org/docs/setup/shared_homeserver.html) or [bare metal](https://cloudinabottle.org/docs/setup/dedicated_homeserver.html))
* [Check out the code on GitHub](https://github.com/cloud-in-a-bottle/cloud-in-a-bottle/)
* [Chat with us on Matrix](https://matrix.to/#/#openhost-community:matrix.openhost.imbue.com)
