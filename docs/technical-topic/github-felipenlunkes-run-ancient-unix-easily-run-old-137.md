---
id: 137
url: https://github.com/felipenlunkes/run-ancient-unix
title: 'GitHub - felipenlunkes/run-ancient-unix: Easily run old versions of UNIX for
  PDP-11 on modern hardware'
domain: github.com
source_date: '2025-11-20'
tags:
- github-repo
- emulator
- cli-tool
- python
summary: This GitHub repository provides tools to run historical UNIX versions on
  modern hardware, including Version 1, 5, and 7 UNIX for PDP-11 systems (via simulator)
  and Version 7 UNIX ported to x86 architecture. To use it, users need to install
  required tools like SIMH, QEMU, and Python, then clone the repository and run the
  setup script to download and install the UNIX disk images before launching their
  chosen UNIX version through either a command-line or Python GUI interface.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - felipenlunkes/run-ancient-unix: Easily run old versions of UNIX for PDP-11 on modern hardware

[![](https://github.com/felipenlunkes/run-ancient-unix/raw/main/doc/banner.png)](https://github.com/felipenlunkes/run-ancient-unix/blob/main/doc/banner.png)

[![](https://camo.githubusercontent.com/83c3a1ed1d62da6b0154f04422bae3339a9fe4da1d89a3bf9071723fcb5da521/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)](https://camo.githubusercontent.com/83c3a1ed1d62da6b0154f04422bae3339a9fe4da1d89a3bf9071723fcb5da521/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)
[![](https://camo.githubusercontent.com/dee5c034ba7ca67c10d850fc85f2d7099479d31cc2a68f23ca436fc4cb595ebc/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)](https://camo.githubusercontent.com/dee5c034ba7ca67c10d850fc85f2d7099479d31cc2a68f23ca436fc4cb595ebc/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)
[![](https://camo.githubusercontent.com/6fc59aed0c0ee939babc6f13c1501ab8ab132edfca32f5efe556c2b821ecbd77/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)](https://camo.githubusercontent.com/6fc59aed0c0ee939babc6f13c1501ab8ab132edfca32f5efe556c2b821ecbd77/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)
[![](https://camo.githubusercontent.com/aafe68d074cd027ac5ca1e829deed91ad20281a947b1ba89ddf444f0b2eacb55/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d636c6f7365642f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)](https://camo.githubusercontent.com/aafe68d074cd027ac5ca1e829deed91ad20281a947b1ba89ddf444f0b2eacb55/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d636c6f7365642f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)
[![](https://camo.githubusercontent.com/9ee71a3674df7170ec998747d9902da09d2c6e3d5a4ddc15707b553f4ae1e661/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)](https://camo.githubusercontent.com/9ee71a3674df7170ec998747d9902da09d2c6e3d5a4ddc15707b553f4ae1e661/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)
[![](https://camo.githubusercontent.com/00ca92d67cc9edae82947e9b05d66588ea3c2402a1036fd60af7a50646a7b861/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722d636c6f7365642f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)](https://camo.githubusercontent.com/00ca92d67cc9edae82947e9b05d66588ea3c2402a1036fd60af7a50646a7b861/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732d70722d636c6f7365642f66656c6970656e6c756e6b65732f72756e2d616e6369656e742d756e69782e737667)
[![](https://camo.githubusercontent.com/dcfe5d9e8ad908bdd5d6094f8ac5ec53177bbc5f68e8b6ba037c31ce594fcc1b/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f6c756e78383038362e7376673f7374796c653d736f6369616c266c6162656c3d466f6c6c6f772532302534306c756e7838303836)](https://twitter.com/lunx8086)

---

Run ancient UNIX on modern hardware
===================================

The contents of this repository allow older versions of [UNIX](https://en.wikipedia.org/wiki/Unix) ([ancient UNIX](https://en.wikipedia.org/wiki/Ancient_UNIX)) to run easily on modern [Unix-like](https://en.wikipedia.org/wiki/Unix-like) systems (Linux, FreeBSD, macOS, among others).

At this time, you can run the following versions of UNIX:

* UNIX versions for [PDP-11](https://en.wikipedia.org/wiki/PDP-11) (run on a PDP-11 simulator):

  + [Version 1 UNIX](https://github.com/jserv/unix-v1);
  + [Version 5 UNIX](https://gunkies.org/wiki/UNIX_Fifth_Edition);
  + [Version 7 UNIX](https://en.wikipedia.org/wiki/Version_7_Unix);
  + [2.11BSD UNIX](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution).
* UNIX versions for x86:

  + [Version 7 UNIX](https://en.wikipedia.org/wiki/Version_7_Unix) ported to x86 architecture by [Robert Nordier](https://www.nordier.com/) (original port in 1999 and patches in 2006-2007).

---



---

License, Credits and Copyright
------------------------------

First of all, credits and acknowledgment for material available in this repository that is not my own (or has been modified by me based on previous work).

* The UNIX versions available in this repository have been released as open source under the [Caldera license](/felipenlunkes/run-ancient-unix/blob/main/doc/Caldera-license.pdf) available in this repository. Please read the document carefully for concrete information about your rights and obligations when using the software.
  + Note that various components within the system images may have been made available under other license conditions. Pay attention to these components. A clear example is version 2.11BSD UNIX, which features code covered by the Caldera license made available, in addition to code released under the [BSD license](/felipenlunkes/run-ancient-unix/blob/main/doc/BSD-license.txt). Source files available in the images show the license and due copyright. Check this data before reuse.
  + The UNIX images available in this repository were obtained from the w11 project (which uses these images for other purposes). You can get them directly [here](https://wfjm.github.io/home/w11/inst/systems.html#h_os_kits), as well as more information about the project, images, licenses and other data.
* The scripts used to simulate the systems using SIMH for v5 and v7 UNIX were obtained from a w11 project repository, which can be accessed [here](https://github.com/wfjm/w11/tree/master/tools/oskit). The original scripts are available under license GLP v3 or later. Modifications in these files were made by me, to fit the purpose of this repository. These modifications are restricted to the same license as the original script.
  + In addition, the general script for configuring the execution environment of versions v5 and v7 was obtained from the project, authored by [Walter F.J. Mueller](https://github.com/wfjm). You can get the original script [here](https://github.com/wfjm/w11/blob/master/tools/simh/setup_w11a_max.scmd). The original script are available under license GLP v3 or later. Modifications in these files were made by me, to fit the purpose of this repository. These modifications are restricted to the same license as the original script.
* The port of Version 7 UNIX to the x86 architecture was performed by [Robert Nordier](https://www.nordier.com/). These modifications are released under the simplified BSD license. For more information on all aspects of the distribution, read [this file](/felipenlunkes/run-ancient-unix/blob/main/v7_x86/LICENSE).
* All my contributions and modifications **(except for material that requires redistribution under the same license, such as the running scripts)** are available in this repository under the BSD-3-Clause [license](/felipenlunkes/run-ancient-unix/blob/main/LICENSE).

---



---

Running UNIX
------------

### Section 1

#### Requeriments

You will need the following tools and utilities to run the available UNIX versions:

[![GNU_Bash](https://camo.githubusercontent.com/08258a2ee3239d2fd9e7208566161e5d77c34263b3f05cf3c3f1092e9fe29892/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f474e55253230426173682d3445414132353f7374796c653d666f722d7468652d6261646765266c6f676f3d474e5525323042617368266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/08258a2ee3239d2fd9e7208566161e5d77c34263b3f05cf3c3f1092e9fe29892/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f474e55253230426173682d3445414132353f7374796c653d666f722d7468652d6261646765266c6f676f3d474e5525323042617368266c6f676f436f6c6f723d7768697465)
[![git](https://camo.githubusercontent.com/e70c2ba9a2ac356a2b7d056994b5778ad687eb92ff982c1fdddb16f5705e53c3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4635373834323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/e70c2ba9a2ac356a2b7d056994b5778ad687eb92ff982c1fdddb16f5705e53c3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769742d4635373834323f7374796c653d666f722d7468652d6261646765266c6f676f3d676974266c6f676f436f6c6f723d7768697465)
[![wget](https://camo.githubusercontent.com/28faac63a2127beb913a3531f5d620a226e85d85a6cc617fbb8d98a686e073e9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f776765742d3030373742353f7374796c653d666f722d7468652d6261646765266c6f676f3d77676574266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/28faac63a2127beb913a3531f5d620a226e85d85a6cc617fbb8d98a686e073e9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f776765742d3030373742353f7374796c653d666f722d7468652d6261646765266c6f676f3d77676574266c6f676f436f6c6f723d7768697465)
[![Python](https://camo.githubusercontent.com/4fa67b3f671b7f19e133c193837c628e78ea1012da04cd7dbca8fb499edd2832/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3834313944313f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/4fa67b3f671b7f19e133c193837c628e78ea1012da04cd7dbca8fb499edd2832/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d3834313944313f7374796c653d666f722d7468652d6261646765266c6f676f3d507974686f6e266c6f676f436f6c6f723d7768697465)
[![qemu](https://camo.githubusercontent.com/3079f301b114e9ed615ce53ba9ec20f956236be0896cb54b8242a98e9ea5d122/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f51656d752d3041304130413f7374796c653d666f722d7468652d6261646765266c6f676f3d71656d75266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/3079f301b114e9ed615ce53ba9ec20f956236be0896cb54b8242a98e9ea5d122/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f51656d752d3041304130413f7374796c653d666f722d7468652d6261646765266c6f676f3d71656d75266c6f676f436f6c6f723d7768697465)
[![SIMH](https://camo.githubusercontent.com/8a01eba613daad37f5424a23143baca3a8b533646e53037e5372df4f76ea3255/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53494d482d4445323231383f7374796c653d666f722d7468652d6261646765266c6f676f3d53494d48266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/8a01eba613daad37f5424a23143baca3a8b533646e53037e5372df4f76ea3255/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53494d482d4445323231383f7374796c653d666f722d7468652d6261646765266c6f676f3d53494d48266c6f676f436f6c6f723d7768697465)

First of all, you must have the `PDP-11 Simulator` (SIMH), `qemu`, `GNU bash`, `Python`, `wget` and `git` installed on your device. If you already have them installed, skip to [section 2](#section-2).

> To install on Debian, Ubuntu, Pop!\_OS and derivatives, use:

```
sudo apt install simh qemu qemu-system-i386 git wget python3 python3-pip python3-tk
```

> To install on Fedora and derivatives, use:

```
sudo dnf install simh qemu qemu-system-i386 git wget python3 python3-pip python3-tkinter
```

> To install on FreeBSD, use (for FreeBSD, installing GNU bash is also required. This shell is not normally installed in a default installation. Installation of GNU bash is not required on Linux systems, where bash is already installed by default):

```
su root # <= Enter your password to login as root user
pkg install -q -y simh bash qemu git wget python3 py39-pip
ln -s /usr/local/bin/pip-3.9 /usr/local/bin/pip
pip install --upgrade pip
```

> To install on NetBSD, use (for NetBSD, installing GNU bash is also required. This shell is not normally installed in a default installation. Installation of GNU bash is not required on Linux systems, where bash is already installed by default):

```
su root # <= Enter your password to login as root user
pkgin install simh bash qemu git wget python3 py39-pip
ln -s /usr/local/bin/pip-3.9 /usr/local/bin/pip
pip install --upgrade pip
```

> To install on OpenBSD, use (for OpenBSD, installing GNU bash is also required. This shell is not normally installed in a default installation. Installation of GNU bash is not required on Linux systems, where bash is already installed by default):

```
su root # <= Enter your password to login as root user
pkg_add simh bash qemu git wget python3 py39-pip
ln -s /usr/local/bin/pip-3.9 /usr/local/bin/pip
pip install --upgrade pip
```

After installation, proceed to [section 2](#section-2).

---

### Section 2

You must clone this repository to your computer. For that, use:

```
git clone https://github.com/felipenlunkes/run-ancient-unix
cd run-ancient-unix
```

After cloning the repository with the configuration files, you must populate the directories of each UNIX version with their respective image files. For that, go to the [next section](#section-3).

---

### Section 3

Now, you have to run the available `run.sh` script. For that, use:

```
chmod +x run.sh
./run.sh
```

First, you have to run the script and select the option to install system images. You can also use the Python frontend to run the script. This is the easiest and simplest way to run script functions. To run this frontend and not rely on the command line, go to [section 5](#section-5). To continue the steps using the terminal, go to [section 4](#section-4).

---

### Section 4

You will see the following screen:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>:
```

In this case, you should select option `7`, which will install the system images. After pressing 7, press ENTER to make your choice effective. Wait for the process of obtaining, extracting, configuring and installing the images.

After the installation is complete, you must run `run.sh` again to start a UNIX version.

When running the script, you will be asked to choose one of the available UNIX versions. After typing only the number relative to the choice, press ENTER to make your decision effective. Then wait for the desired version to run.

Now, you need to know peculiarities in the execution of each version of the system. For this, go to [section 6](#section-6).

---

### Section 5

You need to start running the Python frontend that will manage the configuration and running of UNIX on your computer. First, you must install the TKinter Python package on your computer. For that, use:

```
pip install tk
```

After that, you can press the `RAU.py` script with the right button of your mouse and select the option of `Run as program` or start the script from the terminal, using:

```
python3 RAU.py
```

> WARNING! The frontend is currently only compatible with the GNOME graphical environment (Linux and BSD systems). You can manually replace the `gnome-terminal` calls with `konsole` or another desired terminal emulator. Feel free to submit a pull request with any improvements or changes to the frontend.

After running the program, you will see the following screen:

[![](https://github.com/felipenlunkes/run-ancient-unix/raw/main/doc/frontend.png)](https://github.com/felipenlunkes/run-ancient-unix/blob/main/doc/frontend.png)

On first run, you must install the UNIX disk images locally on your computer. Prior to this operation, you will NOT be able to run UNIX. To do so, click on the `Install UNIX system images` button.

After downloading and installing the disk images, you are able to run UNIX. To do so, select the desired UNIX version in the `Running options` section of the frontend screen.

Go to the [next section](#section-6) for more information about the specifics of running each version of UNIX available. Remember that when using the Python frontend, the command line selection screen, as shown in the next section, will not be displayed. However, the manual options and settings presented in the next section (after the selection screen, which will not appear) are still required to run each version of UNIX.

---

### Section 6

Select the desired UNIX version option below for details on how to start and operate the system. Each version of UNIX has different boot procedures. Pay attention to each particularity.

Particularities for Version 1 UNIX

#### Particularities for Version 1 UNIX

After the start of execution after selecting v1 version, you will see a screen like below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 1

PDP-11 simulator V3.8-1
Disabling CR
Disabling XQ
RF: buffering file in memory
TC0: 16b format, buffering file in memory

:login:
```

Just type `root`, in lower case, and press ENTER. You will immediately be taken to the UNIX v1 shell.

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 1

PDP-11 simulator V3.8-1
Disabling CR
Disabling XQ
RF: buffering file in memory
TC0: 16b format, buffering file in memory

:login: root
root
# ls
bin
dev
etc
tmp
usr
#
```

To end the simulation, press CTRL-E followed by CTRL-C or by typing quit when the `simh>` prompt appears on the screen.


Particularities for Version 5 UNIX

#### Particularities for Version 5 UNIX

After the start of execution after selecting v5 version, you will see a screen like below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 2

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
@
```

To start UNIX, you must type `unix` and press ENTER after the @ character, without spaces and in lower case. After pressing ENTER, UNIX will load and you will be taken to a login screen as below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 2

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
@unix

login:
```

You must then type `root` and press ENTER. You will then be taken to the shell and be able to use the system. See below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 2

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
@unix

login: root
#
```

To end the simulation, press CTRL-E followed by CTRL-C or by typing quit when the `simh>` prompt appears on the screen.


Particularities for Version 7 UNIX

#### Particularities for Version 7 UNIX

After the start of execution after selecting v7 version, you will see a screen like below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 3

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
```

After seeing the screen above, you must type `boot` in lower case and press ENTER. You will see the screen below after that:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 3

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
boot
Boot
:
```

After the appearance of `:`, you must type, without spaces and in lower case, the command `hp(0,0)unix` and press ENTER, as below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 3

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
boot
Boot
: hp(0,0)unix
mem = 2020544
#
```

Pressing ENTER will immediately take you to the UNIX v7 shell.

* To enter multiuser mode and access all system functions, press CTRL-D. Afterwards, provide `root` as username and password. You will again be taken to the UNIX v7 shell, as below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 3

PDP-11 simulator V3.8-1
Disabling XQ
Logging to file "simh_dl0.log"
Listening on port 5671 (socket 5)
Listening on port 5672 (socket 7)
Modem control activated
boot
Boot
: hp(0,0)unix
mem = 2020544
# RESTRICTED RIGHTS: USE, DUPLICATION, OR DISCLOSURE
IS SUBJECT TO RESTRICTIONS STATED IN YOUR CONTRACT WITH
WESTERN ELECTRIC COMPANY, INC.
WED DEC 31 19:05:14 EST 1969

login: root
Password:
You have mail.
#
```

To end the simulation, press CTRL-E followed by CTRL-C or by typing quit when the `simh>` prompt appears on the screen.


Particularities for 2.11BSD UNIX

#### Particularities for 2.11BSD UNIX

After the start of execution after selecting 2.11BSD UNIX version, you will see a screen like below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 4

PDP-11 simulator V3.8-1
Listening on port 4000 (socket 4)
Modem control activated
Auto disconnect activated
211bsd.simh> attach xq eth0
File open error
Disabling CR

73Boot from ra(0,0,0) at 0172150
:
```

You can just press ENTER when you see the screen to start UNIX. Afterwards, you will see the following screen:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 4

PDP-11 simulator V3.8-1
Listening on port 4000 (socket 4)
Modem control activated
Auto disconnect activated
211bsd.simh> attach xq eth0
File open error
Disabling CR

73Boot from ra(0,0,0) at 0172150
: 
: ra(0,0,0)unix
Boot: bootdev=02400 bootcsr=0172150

2.11 BSD UNIX #1: Fri Jun 9 08:42:54 PDT 1995
    root@SSU-64EN137:/usr/src/sys/SYSTEM

ra0: Ver 3 mod 3
ra0: RD54  size=311200
attaching qe0 csr 174440
qe0: DEC DELQA addr 00:50:56:01:01:01
attaching lo0

phys mem  = 3145728
avail mem = 1737664
user mem  = 307200

June  9 12:21:04 init: configure system

dz 0 csr 160100 vector 300 attached
ra 0 csr 172150 vector 154 vectorset attached
ts 0 csr 172520 vector 224 attached
erase, kill ^U, intr ^C
#
```

The `#` symbol indicates that the shell is ready to receive commands. Try using `uname -a` or `ls` to get started.

* To enter multiuser mode and access all system functions, press CTRL-D. Afterwards, provide `root` as username and password. You will again be taken to the 2.11BSD shell.

To end the simulation, press CTRL-E followed by CTRL-C or by typing quit when the `simh>` prompt appears on the screen.


Particularities for Version 7 UNIX for x86

#### Particularities for Version 7 UNIX for x86

After the start of execution after selecting v7 UNIX for x86, you will see a screen like below:

```
You must select, from the list below, which edition/version of
UNIX you want to start. The available options are:

1) v1 UNIX
2) v5 UNIX
3) v7 UNIX
4) 2.11BSD UNIX
5) v7 UNIX for x86
6) Clear temporary files
7) Install the disk images for UNIX

Select a number and press <ENTER>: 5
```

Upon selection, `qemu` will automatically start with the Version 7 UNIX for x86 disk image. After the initial boot, you will see the following screen:

[![](https://github.com/felipenlunkes/run-ancient-unix/raw/main/doc/qemu1.png)](https://github.com/felipenlunkes/run-ancient-unix/blob/main/doc/qemu1.png)

Then press ENTER to load and start UNIX. After pressing ENTER, you will see the following screen, and you will be able to interact with the Version 7 UNIX shell:

[![](https://github.com/felipenlunkes/run-ancient-unix/raw/main/doc/qemu2.png)](https://github.com/felipenlunkes/run-ancient-unix/blob/main/doc/qemu2.png)

* To enter multiuser mode and access all system functions, press CTRL-D. Afterwards, provide `root` as username and `password` as password. You will again be taken to the Version 7 UNIX shell.

When you are finished running the system on the PDP-11 simulator, you can clean up temporary and log files that may have been created by SIMH. To do so, go to [section 7](#section-7).

---

### Section 7

The simulator can create temporary and log files to simulate peripheral devices that would be connected to a PDP-11 minicomputer. These files typically have `.log` and `.dat` extensions. You can remove these files using the `run.sh` script and selecting the cleanup temporary files option, as well as manually going into each system directory and entering, in your system shell:

```
cd UNIX_VERSION_DIRECTORY
rm *.log *.dat
cd ..
```
