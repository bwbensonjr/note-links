---
id: 524
url: https://til.simonwillison.net/github-actions/github-pages
title: Building and deploying a custom site using GitHub Actions and GitHub Pages
  | Simon Willison’s TILs
domain: til.simonwillison.net
source_date: '2025-03-19'
tags:
- github-repo
- devops
- tutorial
- web-dev
summary: This guide demonstrates a minimal pattern for building and deploying a custom
  website using GitHub Actions and GitHub Pages. The key steps are enabling GitHub
  Pages with "GitHub Actions" as the build source, creating a workflow YAML file that
  builds your site into a `_site/` directory, and using the `actions/upload-pages-artifact`
  and `actions/deploy-pages` actions to deploy it. The approach can be combined with
  scheduled workflows and Git scraping to create dynamic sites like RSS feeds or data-driven
  projects.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Building and deploying a custom site using GitHub Actions and GitHub Pages | Simon Willison’s TILs

Building and deploying a custom site using GitHub Actions and GitHub Pages I figured out a minimal pattern for building a completely custom website using GitHub Actions and deploying the result to GitHub Pages. First you need to enable GitHub Pages for the repository. Navigate to Settings -> Pages (or visit $repo/settings/pages ) and set the build source to "GitHub Actions". Here's my minimal YAML recipe - save this in a .github/workflows/publish.yml file: name : Publish site on : push : workflow_dispatch : permissions : contents : read pages : write id-token : write jobs : build : runs-on : ubuntu-latest steps : - uses : actions/checkout@v4 - name : Build the site run : | mkdir _site echo '<h1>Hello, world!</h1>' > _site/index.html - name : Upload artifact uses : actions/upload-pages-artifact@v3 deploy : environment : name : github-pages url : ${{ steps.deployment.outputs.page_url }} runs-on : ubuntu-latest needs : build steps : - name : Deploy to GitHub Pages id : deployment uses : actions/deploy-pages@v4 Anything that goes in that _site/ directory will be published to the GitHub Pages site. The permissions are required: contents: read allows the actions/checkout action to check out the repo pages: write enables writes to pages id-token: write one is needed by the actions/deploy-pages action for some reason The default URL for the site will be https://$GITHUB_USERNAME.github.io/$REPO_NAME/ . You can set this to custom domain if you want. github.com/simonw/minimal-github-pages-from-actions is an example repository that uses this exact YAML configuration. It publishes a site to https://simonw.github.io/minimal-github-pages-from-actions/ . Next steps You can combine this trick with scheduled workflows and Git scraping to create all sorts of interesting and useful things. I'm using it to publish an Atom feed of recent California Brown Pelicans sightings on iNaturalist in my simonw/recent-california-brown-pelicans repository. I also use it to publish my tools.simonwillison.net site with a custom colophon page - see this post for details. Created 2025-03-18T12:52:27-07:00, updated 2025-07-23T21:54:42-07:00 · History · Edit
