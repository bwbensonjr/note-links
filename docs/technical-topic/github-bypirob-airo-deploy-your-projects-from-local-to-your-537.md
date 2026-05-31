---
id: 537
url: https://github.com/bypirob/airo
title: 'GitHub - bypirob/airo: Deploy your projects from local to your production
  VPS.'
domain: github.com
source_date: '2025-03-09'
tags:
- github-repo
- devops
- cli-tool
- python
summary: Airo is a deployment tool that simplifies deploying Docker containers from
  your local machine directly to a production VPS via SSH or a registry, configured
  through an `airo.yaml` file. It's designed as a lightweight alternative to Kubernetes
  and PaaS solutions, offering easier automation and greater server control for developers
  who prefer managing their own infrastructure. The tool provides simple commands
  for building, pushing, deploying, and managing containerized applications with minimal
  configuration overhead.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# GitHub - bypirob/airo: Deploy your projects from local to your production VPS.

🚀 Airo Deploy your projects directly from your local computer to your production server (VPS) easily. Airo builds Docker images and deploys them over SSH or via a registry, driven by airo.yaml . Why Airo? Deploying side-projects doesn't have to be complicated or expensive. Kubernetes, Platform as a Service (PaaS) and CI/CD pipelines are a powerful and exciting solutions, but sometimes they're more complex than your project requires. If you enjoy managing your server, it can be significantly cheaper and offer greater control over the technical details. I want to automate this process and deploy easily to my own server. That's why I've created Airo : 🚀 Focus on building your product , not managing infrastructure. 🐳 Build and deliver Docker images via a registry or direct copy . ⚡️ Deploy instantly with a single command from your computer. 🔑 Easily update configurations and containers securely using SSH. Installation From Source git clone https://github.com/bypirob/airo.git cd airo make install Usage Configure airo.yaml name : airo container : target_arch : linux/amd64 port : 3000 app_port : 3000 deploy : type : ssh # or registry env_file : " /etc/airo/app.env " networks : - " frontend " - " backend " ssh : host : " 192.168.1.100 " user : " admin " port : 22 identity_file : " ~/.ssh/id_rsa " registry : registry_url : " registry.example.com " repository : " my-app " Commands airo build --tag airo:dev --context . airo push --tag airo:dev airo deploy --tag airo:dev airo status airo tags airo tags --remote airo release --tag airo:dev --context . airo version Project and config paths By default, airo reads airo.yaml from the current directory. You can point to a different project root or config file: airo build --project /path/to/project --config airo.yaml
