---
id: 549
url: https://github.com/Shemnei/punktf
title: 'GitHub - Shemnei/punktf: ⚡ A cross-platform multi-target dotfiles manager'
domain: github.com
source_date: '2025-03-02'
tags:
- github-repo
- cli-tool
- rust
- devops
summary: '**Punktf** is a cross-platform dotfiles manager that allows users to manage
  and deploy configuration files across multiple machines and operating systems (Windows,
  Linux, Arch, etc.) from a single source. It enables users to compile and deploy
  dotfiles with conditional logic using handlebar-like templates, pre/post-hooks,
  and multiple profiles tailored to different targets. The tool is available on multiple
  package managers (Homebrew, AUR, Scoop, Chocolatey) and can be installed via Cargo
  or built from source.'
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - Shemnei/punktf: ⚡ A cross-platform multi-target dotfiles manager

punktf - A multi-target dotfiles manager Yet another dotfile manager?! Well, yes, but hear me out: This project was driven by the personal need of having to manage several dotfiles for different machines/targets. You want the same experience everywhere: On your Windows workstation along with an Ubuntu WSL instance, your Debian server and your private Arch installation. This tool fixes that problem while being cross-platform and blazingly fast. You won't need multiple sets of dotfile configurations ever again! Features: Compile and deploy your dotfiles with one command across different platforms Use handlebar-like instructions to insert variables and compile sections conditionally Define pre- and post-hooks to customize the behavior with your own commands Create multiple profiles for different targets Works on Windows and Linux Installation Homebrew Install punktf using Homebrew on Linux: brew install michidk/tools/punktf AUR Install punktf from AUR on Arch Linux. To install it use your favorite AUR capable package manager (e.g. yay , pikaur ): NOTE: As this builds punktf from source an up-to-date rust installation is needed. yay punktf or pikaur -S punktf Scoop Install punktf using Scoop on Windows: scoop bucket add shemnei https://github.com/Shemnei/scoop-bucket scoop install punktf Chocolatey Install punktf using Chocolatey on Windows: choco install punktf Cargo & Crates.io Install punktf using cargo and crates.io on Windows and Linux: cargo install punktf Building from source To install punktf from source the following is needed: An up-to-date rust installation An installed nightly toolchain # Clone git clone https://github.com/Shemnei/punktf cd punktf # Build (cargo) cargo build --release Usage Commands To deploy a profile, use the deploy subcommand: # deploy 'windows' profile punktf deploy --profile windows # deploy (custom source folder) punktf deploy --source /home/demo/mydotfiles --profile windows Adding the -h / --help flag to a given subcommand, will print usage instructions. Source Folder The punktf source folder is the folder containing the dotfiles and punktf profiles. We recommend setting the PUNKTF_SOURCE environment variable so that the dotfiles can be compiled using punktf deploy <profile> . punktf searches for the source folder in the following order: Paths specified with -s / --source Paths specified by an environment variable PUNKTF_SOURCE The current working directory of the shell The source folder should contain two sub-folders: profiles\ : Contains the punktf profile definitions ( .yaml or .json ) dotfiles\ : Contains folders and the actual dotfiles Example punktf source folder structure: + profiles + windows .yaml + base .yaml + arch .json + dotfiles + .gitconfig + init .vim.win + base + demo .txt + linux + .bashrc + windows + alacritty .yml Target Determines where punktf will deploy files too. It can be set with: Variable target in the punktf profile file Environment variable PUNKTF_TARGET Profiles Profiles define which dotfiles should be used. They can be a .json or .yaml file. Example punktf profile: variables : OS : " windows " target : " C: \\ Users \\ Demo " dotfiles : - path : " base " - path : " windows/alacritty.yml " target : path : " C: \\ Users \\ Demo \\ AppData \\ Local \\ alacritty.yml " merge : Ask links : - source_path : " C: \\ Users \\ Demo \\ Dotfiles \\ test.txt " target_path : " C: \\ Users \\ Demo \\ test.txt " All properties are explained in the wiki . Templates Please refer to the wiki for the templating syntax. License Licensed under either of Apache License, Version 2.0, ( LICENSE-APACHE or https://www.apache.org/licenses/LICENSE-2.0 ) MIT license ( LICENSE-MIT or https://opensource.org/licenses/MIT ) at your option. Contribution Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you, as defined in the Apache-2.0 license, shall be dual licensed as above, without any additional terms or conditions.
