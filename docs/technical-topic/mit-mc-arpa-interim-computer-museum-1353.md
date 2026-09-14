---
id: 1353
url: https://icm.museum/blog/?p=38
title: MIT-MC.ARPA – INTERIM COMPUTER MUSEUM
domain: icm.museum
source_date: '2026-09-13'
tags:
- ai
- academic-paper
- distributed-systems
- lisp
summary: MIT-MC.ARPA was a DECSYSTEM-10 KL10 computer operated by the MIT MACSYMA
  Consortium from 1975 to 1988 that served as a pioneering platform for artificial
  intelligence and symbolic computation research during the 1970s and early 1980s.
  The system ran the Incompatible Timesharing System (ITS) and hosted MACSYMA, a groundbreaking
  symbolic algebra system developed from 1968-1982 that demonstrated the potential
  of symbolic AI through sophisticated mathematical capabilities. As a major ARPANET
  node with extensive memory, disk storage, and network connectivity, MIT-MC facilitated
  collaborative research and remote access for programmers and researchers, making
  it central to advancing interactive computing and large-scale symbolic programming.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# MIT-MC.ARPA – INTERIM COMPUTER MUSEUM

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_2165-Large-1024x835.jpeg)

MIT-MC.ARPA was a DECSYSTEM-10 KL10 Model 1080 operated by the MIT MACSYMA Consortium, serving as one of the most significant systems in the development of AI and symbolic computation during the 1970s and early 1980s. Running the Incompatible Timesharing System (ITS), MC provided a uniquely open and collaborative computing environment where many pioneering software systems were developed. As a major ARPANET node, it allowed remote access and encouraged experimentation by a community of programmers, researchers, and students. The system’s flexibility and accessibility made it a central platform for advancing interactive computing and large-scale symbolic programming.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_2163-Large-768x1024.jpeg)

One of the most influential software systems developed and run on MIT-MC was **MACSYMA**, a powerful symbolic algebra system.  It was originally developed from 1968 to 1982 at [MIT](https://en.wikipedia.org/wiki/MIT)‘s [Project MAC](https://en.wikipedia.org/wiki/Project_MAC). MACSYMA was built on top of the lisp dialect, MACLISP and was one of the most advanced symbolic manipulators of its time.

The project was initiated in July, 1968 by Car Engelman, William Martin, and Joel Moses. Engelman and Martin were largely responsible for the front end, expression display, and polynomial arithmetic. Moses implemented the simplifier, the indefinite integration support, and Macsyma heuristics, including Risch support. Martin was in charge of the project until 1971, and Moses ran it for the next decade. The integration of sophisticated mathematical capabilities with efficient system design demonstrated the potential of symbolic AI and laid groundwork for future mathematical software. MACSYMA became a landmark achievement in symbolic computing.   
  
Macsyma was initiated by MIT’s Project MAC, established in 1963 within the Department of Electrical Engineering (later renamed to the Department of Electrical Engineering and Computer Science). Funding was provided by the Defense Advanced Research Projects Agency (DARPA). Project MAC became became MIT’s Lab for Computer Science (LCS) in 1976. One of Project MAC’s major undertakings was the development of Macsyma. Development began on a PDP-10 KA, running ITS (Incompatible Timesharing System). Eventually, due to increased performance needs, Project MAC purchased from Digital Equipment Corporation (DEC) a PDP-10 KL around 1975. This machine was named MIT-MC, where MC stood for Macsyma Consortium. It also ran the ITS operating system, as did the other PDP-10s at MIT’s AI Lab, Math Lab, and Dynamic Modeling Group. MIT-MC’s KL10 had serial number 1038, and was in service at MIT from 1975 to 1988.

The KL10 was outfitted with a hardware addition called the **KL-UDGE**. The name is a play on the word *kludge*, meaning a workaround or hack. It provided a real-time calendar clock, an IMP interface for connecting to the ARPANET, and 36 software programmable lights, since the KL10 didn’t sport any. The real-time calendar clock was called the DeCoriolis Clock, named after Paul DeCoriolis, and the TS program to set the clock, PDSET, bore DeCoriolis’ initials. The other ITS systems, running on the KA10, didn’t need the KL-UDGE, because the real time clock functionality was built into the KA10. The DeCoriolis Clock interface was built on top of this real-time clock for the non-KL10 ITS systems.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_4422-Large-1024x806.jpeg)

The KL-UDGGE is a prime example of the MIT hacker ethic: elegant or not, the goal was to make the system *work better*, even if it meant bending the rules of conventional hardware design.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_7047-3-Large-1024x744.jpeg)
![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_1849-Large-1024x768.jpeg)

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_1850-Large-1024x768.jpeg)

MIT-MC was added to the ARPANET in 1976. The email message from Dave Moon, below, announces this event:

```
Date: 14 FEB 1976 0035-EST
From: MOON at MIT-MC
To: NETWORK-LIAISON-GROUP at MIT-MC, *** at MIT-MC
CC: JM at MIT-MC, Feinler at BBN-TENEXB, JM at MIT-ML

MIT-MC (the Macsyma Consortium KL10) is now on the Arpanet
as host number 354 (octal) or 236 decimal. Note that this
is DIFFERENT FROM the host number in the Resource Notebook.
```

The following excerpt from a April 1980 Project MAC report, written by Ellen Golden, includes:

```
The primary hardware improvement this past year was the addition of a million words of memory to the MC machine, bringing the total available memory
to 1.5 million words. The primary effect of this addition was
to increase the ratio of cpu time to connect time by about 50%.
A secondary effect was that the number of connect hours increased, probably due
to the enhanced performance of the system.

In order to handle the increased demand for secondary storage, a new 300 megabyte disk drive will soon be added to the 3 RP04s now online.
In addition, a LISP Machine (developed by the M.I.T. Artificial Intelligence
Laboratory) will be made available for use by MACSYMA users.
```

MIT-MC eventually had 2MW (2048 1K words) of memory. which was enough to support 120 concurrent ITS jobs. It had 6 disk units, 3 of which were RP04 disks and 3 of which were Trident T-300 disks. The disks supported 500 user directories. The RP04s were connected via an RH10 disk controller. The T-300s were connected to a slave PDP-11 that shared memory with the KL10. It had 1 magnetic tape unit, a DF10-based TM10B. It had a DL10 tty controller, with 4 DC76 TTYs attached. It also had 33 DTE20 TTYs. In addition, there were 25 pseudo-ttys (STYs) for various uses, including network connections.

MIT-MC had both an Internet connection and a CHAOS net connection. Originally, it had an ARPANET connection, with an ARPA host number of 106, but this was replaced with Internet support once Internet protocols became available. The IP address of MIT-MC was 10.1.0.6 and MIT-MC supported 25 concurrent TCP connections. It’s chaosnet address was 1440, and the chaos interface supported 30 concurrent CHAOS net connections. The CHAOS net interface went through the DL10 tty controller and to an attached PDP-11. The PDP-11 ran a CHAOS net router/terminal concentrator called NSWIT, or New Switch. It’s similar to MINITS, but older. NSWIT may have started at MIT, but was later mainly in use at the S-1 project at Lawrence Livermore National Laboratory (often called LLL).

MIT-MC (and other ITS systems) had a DeCoriolis Clock, which interrupted the KL10 CPU at a frequency of 60 Hz. The DeCoriolis clock was named after Paul DeCoriolis, and the ITS program to set the clock, PDSET, bore DeCoriolis’ initials.

While the Xerox Graphics Printer (XGP) was connected to the MIT-AI KA10, MIT-MC had an indirection connection to the Xerox Dover printer. (MIT-MC users could also spool to the MIT-AI XGP printer). The Dover printer was connected to a Xerox Alto using Ethernet hardware. Thus, it was necessary to use EFTP to talk to the Dover spooler, running on a Xerox Alto machine called SPRUCE. Since ITS knew how to talk TCP and CHAOS, and had no means of directly generating Ethernet packets, a gateway machine (LCS-gateway) was used to translate the CHAOSNET packets to Ethernet packets.

There was a also an ITS-side Dover spooler running on MIT-MC, so that uses could queue jobs for the Dover printer, and the spooler would feed files to SPRUCE from the queue. SPRUCE, in turn, would send the files to the Dover printer.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_3059-Large-1024x822.jpeg)

The service card attached to MC’s CPU bay 2.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_3063-Large-1024x768.jpeg)

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_3061-Large-1024x768.jpeg)

An “END OF DEC(K)” punched card from MIT with the K blocked out by a white label.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_3056-Large-1024x849.jpeg)

1200 Volt! – Preventive maintenance.

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_7046-2-Large-1024x768.jpeg)

![](https://icm.museum/blog/wp-content/uploads/2025/06/IMG_7145-1024x1024.jpg)

*“It takes more than good memory to have good memories.*” cites a fortune from Mary Chung’s restaurant in Cambridge.

Support for the preservation of MC is made possible through our [Sponsor a Computer](https://icm.museum/?donate) program.
