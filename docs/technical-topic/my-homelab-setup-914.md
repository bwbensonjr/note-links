---
id: 914
url: https://bryananthonio.com/blog/my-homelab-setup/
title: My Homelab Setup
domain: bryananthonio.com
source_date: '2026-03-09'
tags:
- devops
- database
- distributed-systems
- ai
summary: The author repurposed an old gaming PC as a home server running TrueNAS to
  solve data storage and backup challenges for their photography files. The setup
  includes 16 TB of mirrored storage, several self-hosted applications like Immich
  for photo management, Mealie for recipes, and Ollama for running AI models locally,
  with remote access enabled through Tailscale VPN. Future improvements include implementing
  custom domain names for easier access to the various services.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# My Homelab Setup

My Homelab Setup
================

How I repurposed my old gaming PC to set up a home server for data storage, backups, and self-hosted apps.

March 7th, 2026 6 min read

![A Fractal Design PC case with the side panel removed, showing an EVGA GeForce GTX 1070 Ti GPU and CPU cooler](/_astro/homelab-pc_u8YoU.jpg)  

My homelab PC

For the longest time, I’ve procrastinated on finding a good backup and storage solution for my Fujifilm RAW files. My solution up until recently involved manually copying my photos across two external SSD drives. This was quite a hassle and I hadn’t yet figured out a good off-site backup strategy.

After hearing constant news updates of how [hard drive prices have been surging due to AI data center buildouts](https://www.pcmag.com/news/memory-shortage-now-wreaking-havoc-on-hard-drive-prices-too), I finally decided to purchase some hard drives and set up a homelab to meet my storage and backup needs. I also used this opportunity to explore self-hosting some apps I’ve been eager to check out.

Contents[#](#contents)
----------------------

* [Hardware](#hardware)
* [TrueNAS Operating System](#truenas-operating-system)
* [Apps I’m Currently Self-hosting](#apps-im-currently-self-hosting)
  + [Scrutiny](#scrutiny)
  + [Backrest](#backrest)
  + [Immich](#immich)
  + [Mealie](#mealie)
  + [Ollama](#ollama)
* [Remote Access](#remote-access)
* [Next Steps](#next-steps)

Hardware[#](#hardware)
----------------------

I repurposed my old gaming PC I built back in 2018 for this use case. This machine has the following specs:

| Component | Product |
| --- | --- |
| CPU | [AMD Ryzen 5 2600X 3.6 GHz 6-Core Processor](https://www.techpowerup.com/cpu-specs/ryzen-5-2600x.c2014) |
| Motherboard | [ASRock B450 Pro4 ATX AM4](https://www.asrock.com/mb/amd/b450%20pro4/index.asp) |
| RAM | [G.Skill Flare X 16 GB (2 x 8 GB) DDR4-3200 CL14](https://www.gskill.com/product/165/170/1535961634/F4-3200C14D-16GFX-EOL) |
| GPU | [EVGA FTW2 GAMING iCX GeForce GTX 1070 Ti 8 GB](https://www.evga.com/products/specs/gpu.aspx?pn=649ba262-3f05-4ff8-9756-9cdc206e7ce6) |
| Case | [Fractal Design Meshify C ATX Mid Tower](https://www.fractal-design.com/products/cases/meshify/meshify-c/) |
| PSU | [SeaSonic PRIME Gold 650 W 80+ Gold](https://seasonic.com/prime-gold/) |
| Storage (HDD) | 2x [Western Digital Red Plus 8 TB 3.5”](https://www.westerndigital.com/products/internal-drives/wd-red-plus-sata-3-5-hdd?sku=WD80EFPX) |
| Storage (SSD) | [Samsung 850 Evo 500 GB 2.5”](https://www.samsung.com/us/computing/memory-storage/solid-state-drives/ssd-850-evo-2-5-sata-iii-500gb-mz-75e500b-am/) |
| Storage (NVMe) | [Western Digital Blue SN550 500 GB M.2-2280](https://www.sandisk.com/en-gb/products/ssd/internal-ssd/wd-blue-sn550-nvme-ssd?sku=WDS500G2B0C-00PXH0) |

I purchased the Western Digital hard drives over the winter holiday break. The other components were already installed on the machine when I originally built it.

TrueNAS Operating System[#](#truenas-operating-system)
------------------------------------------------------

On this machine I installed [TrueNAS Community Edition](https://www.truenas.com/truenas-community-edition/) on my NVMe drive. It’s a Linux-based operating system that is well-tailored for network-attached storage (NAS), file storage that is accessible to any device on your network.

 ![The TrueNAS Community Edition dashboard showing system information, CPU usage, and memory stats](/_astro/truenas-dashboard_6BIlH.webp) 

My TrueNAS dashboard running version 25.10.1 (Goldeye)

 

For instance, TrueNAS allows you to create snapshots of your data. This is great for preventing data loss. If, for example, you accidentally deleted a file, you could recover it from a previous snapshot containing that file. In other words, a file is only truly deleted if and only if the system has no snapshots containing that file.

I’ve set up my machine to take hourly, daily, and even weekly snapshots. I’ve also configured it to delete old snapshots after a given period of time to save storage space.

Most of my data is mirrored across the two 8 TB hard disks in a RAID 1 setup. This means that if one drive fails, the other drive will still have all of my data intact. The SSD is used to store data from services that I self-host that benefit from having fast read and write speeds.

Apps I’m Currently Self-hosting[#](#apps-im-currently-self-hosting)
-------------------------------------------------------------------

Not only is TrueNAS good for file storage, you can also host apps on it!
[TrueNAS offers a catalog of apps](https://apps.truenas.com/catalog/), supported by the community, that you can install on your machine.

### Scrutiny[#](#scrutiny)

[Scrutiny](https://github.com/Starosdev/scrutiny) is a web dashboard for monitoring the health of your storage drives. Hard drives and SSDs have built-in firmware called S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology) that continuously tracks health metrics like temperature, power-on hours, and read errors.

Scrutiny reads this data and presents it in a dashboard showing historical trends, making it easy to spot warning signs that a drive may fail soon.

 ![Scrutiny drive health dashboard showing four drives — two 7.3 TiB HDDs, one SSD, and one NVMe — all with a passed status](/_astro/scrutiny-dashboard_ZOyVNT.webp) 

Scrutiny monitoring all four of my drives

 

### Backrest[#](#backrest)

[Backrest](https://garethgeorge.github.io/backrest/) is a web frontend for [restic](https://restic.net), a command-line tool used for creating file backups. I’ve set this up to save daily backups of my data to an object storage bucket on [Backblaze B2](https://www.backblaze.com/cloud-storage).

 ![The Backrest dashboard summary showing backup stats for a media-backup repository and plan](/_astro/backrest-dashboard_1ArxY9.webp) 

My Backrest configuration

 

### Immich[#](#immich)

[Immich](https://immich.app) is one of the most popular open-source self-hosted apps for managing photos and videos. I love that it also offers [iOS](https://apps.apple.com/us/app/immich/id1613945652) and [Android](https://play.google.com/store/apps/details?id=app.alextran.immich&hl=en_US) apps that allow you to back up photos and videos from your mobile devices. This is great if you want to rely less on services like Google Photos or iCloud. I’m currently using this to back up photos and videos from my phone.

 ![Immich photo library showing a grid of bird photos.](/_astro/immich-dashboard_Z6oGg0.webp) 

A sample of my Immich photo library

 

### Mealie[#](#mealie)

[Mealie](https://mealie.io) is a recipe management tool that has made my meal prepping experience so much better! I’ve found it great for saving recipes I find on sites like [NYT Cooking](https://cooking.nytimes.com).

When importing recipes, you can provide the URL of the recipe and Mealie will scrape the ingredients and instructions from the page and save it in your recipe library. This makes it easier to keep track of recipes you find online and want to try out later.

 ![Mealie’s recipe library showing six saved recipes in a grid layout](/_astro/mealie-dashboard_Z1KbX6o.webp) 

A few of my saved recipes in Mealie

 

### Ollama[#](#ollama)

[Ollama](https://ollama.com) is a backend for running various AI models. I installed it to try running large language models like [`qwen3.5:4b`](https://ollama.com/library/qwen3.5:4b) and [`gemma3:4b`](https://ollama.com/library/gemma3:4b) out of curiosity. I’ve also recently been exploring the world of vector embeddings such as [`qwen3-embedding:4b`](https://ollama.com/library/qwen3-embedding:4b). All of these models are small enough to fit in the 8GB of VRAM my GPU provides. I like being able to offload the work of running models on my homelab instead of my laptop.

Remote Access[#](#remote-access)
--------------------------------

When I’m not at home, I use [Tailscale](https://tailscale.com), a plug-and-play VPN service, to access my data and self-hosted apps remotely from any device. Tailscale builds on top of another tool called [WireGuard](https://www.wireguard.com) to provide a secure tunnel into my home network.

The advantage here is that my homelab PC doesn’t need to be exposed to the public internet for this to work. Any device I want to use to access my homelab remotely needs to install the Tailscale app and be authenticated to my Tailscale network.

Next Steps[#](#next-steps)
--------------------------

Right now, accessing my apps requires typing in the IP address of my machine (or Tailscale address) together with the app’s port number. Because all of my services share the same IP address, my password manager has trouble distinguishing which login to use for each one.

In the future I’ll look into figuring out how to assign custom domain names to all of my services.

---

> Recently got into self-hosting. Here’s a write-up of my setup.
>
> — Bryan Anthonio ([@banthonio.com](https://bsky.app/profile/did:plc:yy22yxuejl44zyocsr6ub7c2?ref_src=embed)) [Mar 8, 2026 at 9:44 AM](https://bsky.app/profile/did:plc:yy22yxuejl44zyocsr6ub7c2/post/3mgkrzy5e3225?ref_src=embed)

### Tags

[homelab](/blog/tags/homelab/)  [self-hosting](/blog/tags/self-hosting/)
