---
id: 295
url: https://dev.to/muhammadasif_cse/setting-up-jetbrains-mono-font-on-ubuntu-is-straightforward-5d8i
title: Setting up JetBrains Mono font on Ubuntu is straightforward - DEV Community
domain: dev.to
source_date: '2025-08-11'
tags:
- tutorial
- devops
summary: This guide provides step-by-step instructions for installing JetBrains Mono
  font on Ubuntu by downloading the font files, copying them to the system fonts directory,
  and updating the font cache. The process involves opening a terminal, navigating
  to the font files, using `sudo cp` to move TTF files to `/usr/share/fonts/truetype/`,
  and running `sudo fc-cache -f -v` to refresh the system's font recognition. After
  completion, users can verify the installation by checking for "JetBrains Mono" in
  any application's font selection menu.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Setting up JetBrains Mono font on Ubuntu is straightforward - DEV Community

1. **Open Terminal**:

   * Press `Ctrl + Alt + T` to open a terminal window.
2. **Navigate to the Font Directory**:

   * Use the `cd` command to navigate to the directory where your font files are located. In your case:

   ```
    cd /home/asif/Downloads/JetBrainsMono-2.304/fonts/ttf
   ```
3. **Copy Font Files to System Fonts Directory**:

   * Copy the font files to your system's TrueType fonts directory using the `sudo cp` command:

   ```
    sudo cp *.ttf /usr/share/fonts/truetype/
   ```
4. **Update Font Cache**:

   * Update the font cache so that Ubuntu recognizes the new fonts:

   ```
    sudo fc-cache -f -v
   ```
5. **Verify Installation**:

   * Open a text editor or any application where you can select fonts.
   * Look for "JetBrains Mono" in the font selection list. If you see it, then the font has been successfully installed.

After completing these steps, you should have JetBrains Mono font installed and ready to use on your Ubuntu system.

Collapse

Expand

[![cleverclover profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2805597%2F86613845-37a3-4bb2-9f3a-650663f31012.jpg)](https://dev.to/cleverclover)

[Om Biradar](https://dev.to/cleverclover)

Om Biradar

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2805597%2F86613845-37a3-4bb2-9f3a-650663f31012.jpg)

Om Biradar](/cleverclover)

Follow

IITian | Coder | Systems enthusiast

* Joined

  Feb 2, 2025

•
[Feb 2 '25
• Edited on Feb 2
• Edited](https://dev.to/mdasif-me/setting-up-jetbrains-mono-font-on-ubuntu-is-straightforward-5d8i#comment-2leij)

Dropdown menu

* [Copy link](https://dev.to/mdasif-me/setting-up-jetbrains-mono-font-on-ubuntu-is-straightforward-5d8i#comment-2leij)
* Hide

I think you should add that `*.ttf` files can be placed in `~/.fonts` directory if you want to install it for your user only.

Also to avoid the clutter in the `usr/share/fonts/truetype` you can better create a folder for JetBrains fonts before moving the `*.ttf` files over there.




Collapse

Expand

[![ahmed_soliman_35f81bfef23 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1582862%2F139a6c46-ae7e-4be8-8619-bfdbc376e3f0.png)](https://dev.to/ahmed_soliman_35f81bfef23)

[Ahmed Soliman](https://dev.to/ahmed_soliman_35f81bfef23)

Ahmed Soliman

[![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1582862%2F139a6c46-ae7e-4be8-8619-bfdbc376e3f0.png)

Ahmed Soliman](/ahmed_soliman_35f81bfef23)

Follow

* Joined

  Jun 6, 2024

•
[Nov 4 '24](https://dev.to/mdasif-me/setting-up-jetbrains-mono-font-on-ubuntu-is-straightforward-5d8i#comment-2ja2d)

Dropdown menu

* [Copy link](https://dev.to/mdasif-me/setting-up-jetbrains-mono-font-on-ubuntu-is-straightforward-5d8i#comment-2ja2d)
* Hide

It works great,Thanks.

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)
