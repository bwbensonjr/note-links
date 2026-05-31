---
id: 63
url: https://www.kasava.dev/blog/everything-as-code-monorepo
title: 'Everything as Code: How We Manage Our Company In One Monorepo | Kasava'
domain: www.kasava.dev
source_date: '2025-12-30'
tags:
- devops
- github-repo
- ai
summary: Kasava manages their entire company—product code, documentation, marketing,
  and internal tools—in a single monorepo to enable AI-native development and eliminate
  synchronization problems. This approach allows AI tools to access complete context
  across all systems, enabling faster updates (e.g., a single JSON change to pricing
  instantly propagates across backend, frontend, marketing site, and docs) and ensuring
  one source of truth. The monorepo also creates a unified shipping culture where
  everything—code, content, and documentation—follows the same Git-based workflow,
  removing friction and making deployment muscle memory.
fetch_status: success
summarizer_model: global.anthropic.claude-haiku-4-5-20251001-v1:0
---

# Everything as Code: How We Manage Our Company In One Monorepo | Kasava

[Back to Blog](/blog)

Introduction
------------

Last week, I updated our pricing limits. One JSON file. The backend started enforcing the new caps, the frontend displayed them correctly, the marketing site showed them on the pricing page, and our docs reflected the change—all from a single commit.

No sync issues. No "wait, which repo has the current pricing?" No deploy coordination across three teams. Just one change, everywhere, instantly.

At Kasava, our entire platform lives in a single repository. Not just the code—*everything*:

```
kasava/                              # 5,470+ files TypeScript files
├── frontend/                       # Next.js 16 + React 19 application
│   └── src/
│       ├── app/                   # 25+ route directories
│       └── components/            # 45+ component directories
├── backend/                        # Cloudflare Workers API
│   └── src/
│       ├── services/              # 55+ business logic services
│       └── workflows/             # Mastra AI workflows
├── website/                        # Marketing site (kasava.ai)
├── docs/                           # Public documentation (Mintlify)
├── docs-internal/                  # 12+ architecture docs & specs
├── marketing/
│   ├── blogs/                     # Blog pipeline (drafts → review → published)
│   ├── investor-deck/             # Next.js site showing investment proposal
│   └── email/                     # MJML templates for Loops.so campaigns
├── external/
│   ├── chrome-extension/          # WXT + React bug capture tool
│   ├── google-docs-addon/         # @helper AI assistant (Apps Script)
│   └── google-cloud-functions/
│       ├── tree-sitter-service/   # AST parsing for 10+ languages
│       └── mobbin-research-service/
├── scripts/                        # Deployment & integration testing
├── infra-tester/                   # Integration test harness
└── github-simulator/               # Mock GitHub API for local dev
```

---

Why This Matters: AI-Native Development
---------------------------------------

This isn't about abstract philosophies on design patterns for 'how we should work.' It's about velocity in an era where products change fast and context matters.

AI is all about context. And this monorepo **is** our company—not just the product.

When our AI tools help us write documentation, they have immediate access to the actual code being documented. When we update our marketing website, the AI can verify claims against the real implementation. When we write blog posts like this one, the AI can fact-check every code example, every number, every architectural claim against the source of truth.

**This means we move faster**:

* **Documentation updates faster** because the AI sees code changes and suggests doc updates in the same context
* **Website updates faster** because pricing, features, and capabilities are pulled from the same config files that power the app
* **Blog posts ship faster** because the AI can run self-referential checks—validating that our "5,470+ TypeScript files" claim is accurate by actually counting them
* **Nothing goes out of sync** because there's only one source of truth, and AI has access to all of it

When you ask Claude to "update the pricing page to reflect the new limits," it can:

1. Read the backend service that enforces limits
2. Check the frontend that displays them
3. Update the marketing site
4. Verify the docs are consistent
5. Flag any blog posts that might mention outdated numbers

All in one conversation. All in one repository.

This is what "AI-native development" actually means: structuring your work so AI can be maximally helpful, not fighting against fragmentation.

**And it reinforces a shipping culture.**

Everything-as-code means everything ships the same way: `git push`. Want to update the website pricing page? `git push`. New blog post ready to go live? `git push`. Fix a typo in the docs? `git push`. Deploy a backend feature? `git push`.

No separate CMSs to log into. No WordPress admin panels. No waiting for marketing tools to sync. No "can someone with Contentful access update this?" The same Git workflow that ships code also ships content, documentation, and marketing. Everyone on the team can ship anything, and it all goes through the same review process, the same CI/CD, the same audit trail.

This uniformity removes friction and removes excuses. Shipping becomes muscle memory.

---

Why Everything in One Repo?
---------------------------

### 1. Atomic Changes Across Boundaries (That AI Can Understand)

When a backend API changes, the frontend type definitions update in the same commit. When we add a new feature, the documentation can ship alongside it. No version mismatches. No "which version of the API does this frontend need?"

**AI can see and validate the entire change in context**.

When we ask Claude to add a feature, it doesn't just write backend code. It sees the frontend that will consume it, the docs that need updating, and the marketing site that might reference it. All in one view. All in one conversation.

**Real example from our codebase—adding Asana integration:**

```
commit: "feat: add Asana integration"
├── backend/src/services/AsanaService.ts
├── backend/src/routes/api/integrations/asana.ts
├── frontend/src/components/integrations/asana/
├── frontend/src/app/integrations/asana/
├── docs/integrations/asana.mdx
└── website/src/app/integrations/page.tsx
```

One PR. One review. One merge. Everything ships together.

**Another example—keeping pricing in sync:**

We have a single `billing-plans.json` that defines all plan limits and features:

```
// frontend/src/config/billing-plans.json (also copied to website/src/config/)
{
  "plans": {
    "free": { "limits": { "repositories": 1, "aiChatMessagesPerDay": 10 } },
    "starter": {
      "limits": { "repositories": 10, "aiChatMessagesPerDay": 100 }
    },
    "professional": {
      "limits": { "repositories": 50, "aiChatMessagesPerDay": 1000 }
    }
  }
}
```

The backend enforces these limits. The frontend displays them in settings. The marketing website shows them on the pricing page. When we change a limit, one JSON update propagates everywhere—no "the website says 50 repos but the app shows 25" bugs.

**And AI validates all of it.** When we update `billing-plans.json`, we can ask Claude to verify that the backend, frontend, and website are all consistent. It reads all three implementations and confirms they match—or tells us what needs fixing.

### 2. Cross-Project Refactoring

Renaming a function? Your IDE finds all usages across frontend, backend, docs examples, and blog code snippets. One find-and-replace. One commit.

### 3. Single Source of Truth

* **Dependencies**: Shared tooling configured once
* **CI/CD**: One pipeline to understand
* **Search**: Find anything with one `grep`

---

The Structure: What Lives Where
-------------------------------

### Core Application

```
frontend/                        # Customer-facing Next.js app
├── src/
│   ├── app/                    # Next.js 15 App Router
│   │   ├── analytics/         # Semantic commit analysis
│   │   ├── bug-reports/       # AI-powered bug tracking
│   │   ├── chat/              # AI assistant interface
│   │   ├── code-search/       # Semantic code search
│   │   ├── dashboard/         # Main dashboard
│   │   ├── google-docs-assistant/
│   │   ├── integrations/      # GitHub, Linear, Jira, Asana
│   │   ├── prd/               # PRD management
│   │   └── ...                # 25+ route directories total
│   ├── components/            # 45+ component directories
│   │   ├── ai-elements/      # AI-specific UI
│   │   ├── bug-reports/      # Bug tracking UI
│   │   ├── dashboard/        # Dashboard widgets
│   │   ├── google-docs/      # Google Docs integration
│   │   ├── onboarding/       # User onboarding flow
│   │   └── ui/               # shadcn/ui base components
│   ├── mastra/               # Frontend Mastra integration
│   └── lib/                  # SDK, utilities, hooks

backend/                        # Cloudflare Workers API
├── src/
│   ├── routes/               # Hono API endpoints
│   ├── services/             # 55+ business logic services
│   ├── workflows/            # Mastra AI workflows
│   │   ├── steps/           # Reusable workflow steps
│   │   └── RepositoryIndexingWorkflow.ts
│   ├── db/                   # Drizzle ORM schema
│   ├── durable-objects/      # Stateful edge computing
│   ├── workers/              # Queue consumers
│   └── mastra/               # AI agents and tools
```

These two talk to each other constantly. Having them in the same repo means:

* API changes include frontend updates
* Type safety across the boundary
* Shared testing utilities

### Marketing Properties

```
website/                        # kasava.ai marketing site
├── src/
│   ├── app/                   # Landing pages, blog
│   ├── components/            # Shared marketing components
│   └── lib/                   # Utilities

marketing/
├── blogs/
│   ├── queue/
│   │   └── drafts/           # Ideas and drafts
│   ├── review/               # Ready for editing
│   └── published/            # Live on the site
├── investor-deck/            # Next.js presentation (not PowerPoint!)
└── email/
    ├── CLAUDE.md             # Email writing guidelines
    └── mjml/                 # 7+ email campaign loops
        ├── loop-1-welcome/
        ├── loop-2-github-connected/
        ├── loop-3-trial-conversion/
        └── ...
```

Yes, even blog posts are code. They're Markdown files with frontmatter, versioned in Git, reviewed in PRs. Email templates are MJML that version controls our entire customer communication system.

Even our investor deck is code — a Next.js 16 static site with 17 React slide components, keyboard navigation, and PDF export. No PowerPoint, no Google Slides. When we update metrics or messaging, it's a code change with full Git history, reviewed in a PR, and deployed with `git push`.

**Why this matters**:

* Marketing can update copy without engineering
* Changes are reviewed and tracked
* Rollback is one `git revert` away
* Email campaigns are testable and diffable

### Documentation

```
docs/                           # Public docs (Mintlify)
├── index.mdx                  # Landing page
├── quickstart.mdx             # Getting started
├── demo-mode.mdx              # Demo mode guide
├── features/                  # Product features
│   ├── ai-chat.mdx
│   ├── code-intelligence.mdx
│   ├── code-search.mdx
│   └── prds.mdx
├── integrations/              # Integration guides
│   ├── github.mdx
│   ├── linear.mdx
│   ├── jira.mdx
│   └── asana.mdx
└── bug-tracking/              # Bug tracking docs

docs-internal/                  # Engineering knowledge base
├── GITHUB_CHAT_ARCHITECTURE.md
├── QUEUE_ARCHITECTURE_SUMMARY.md
├── UNIFIED_TASK_ANALYTICS_QUEUE.md
├── features/                  # Feature specs
├── migrations/                # Migration guides
├── plans/                     # Implementation plans
└── research/                  # Research notes
```

Public docs deploy automatically when we push. Internal docs are searchable alongside code—when someone asks "how does the queue work?", they find the actual architecture document, not a stale wiki page.

### External Services

```
external/
├── chrome-extension/          # WXT-based bug capture tool
│   ├── entrypoints/          # popup, content scripts, background
│   ├── lib/                  # Screen capture, console logging
│   ├── components/           # React UI components
│   └── wxt.config.ts         # WXT configuration
│
├── google-docs-addon/        # @helper mentions in Docs
│   ├── Code.gs              # Main Apps Script (18KB)
│   ├── Sidebar.html         # React-like UI (26KB)
│   ├── Settings.html        # Configuration UI
│   └── appsscript.json      # Manifest
│
└── google-cloud-functions/
    ├── tree-sitter-service/  # AST parsing
    │   └── Supports: JS, TS, Python, Go, Rust,
    │       Java, C, C++, Ruby, PHP, C#
    └── mobbin-research-service/  # UX research
```

These deploy to completely different platforms (Chrome Web Store, Google Apps Script, GCP) but live together because:

* They share API contracts with the main app
* Changes often span boundaries
* One team maintains everything

### Development Infrastructure

```
github-simulator/              # Mock GitHub API for local dev
infra-tester/                  # Integration test harness
scripts/
├── google-cloud/             # GCP deployment scripts
├── test-credentials.ts       # Credential testing
└── test-webhook-integration.ts
```

Local development shouldn't require external services. Mock servers live with the code they simulate.

---

What Deploys Where
------------------

| Component | Tech Stack | Deploys To |
| --- | --- | --- |
| Frontend | Next.js 15, React 19, Tailwind v4 | Vercel |
| Backend | Cloudflare Workers, Hono, Mastra | Cloudflare |
| Website | Next.js, custom components | Vercel |
| Investor Deck | Next.js, custom components | Vercel |
| Docs | Mintlify MDX | Mintlify |
| Chrome Extension | WXT, React, Tailwind | Chrome Web Store |
| Google Docs Add-on | Apps Script, HTML | Google Workspace Marketplace |
| Tree-sitter Service | Node.js, GCP Functions | Google Cloud |
| Email Templates | MJML | Loops.so |

---

How We Make It Work
-------------------

### No Workspaces (And That's Fine)

We deliberately don't use npm/yarn workspaces. (Well, we do in *one* specific use case but that's for another post.) Each directory is its own independent npm project:

```
cd frontend && npm install    # Frontend dependencies
cd backend && npm install     # Backend dependencies
cd external/chrome-extension && npm install  # Extension dependencies
```

Why? Simplicity. No hoisting confusion. No "which version of React am I actually getting?" Each project is isolated and predictable.

### Selective CI/CD

We run 5 GitHub Actions workflows, each triggered by specific paths:

```
# .github/workflows/frontend-tests.yml
name: Frontend Tests
on:
  push:
    paths:
      - "frontend/**"
      - ".github/workflows/frontend-tests.yml"
# Runs: type-check, lint, demo data validation, tests with coverage
```

```
# .github/workflows/backend-tests.yml
name: Backend Tests
on:
  push:
    paths:
      - "backend/**"
      - ".github/workflows/backend-tests.yml"
# Runs: unit tests, integration tests, e2e tests
```

```
# .github/workflows/tree-sitter-tests.yml
name: Tree-sitter Tests
on:
  push:
    paths:
      - "external/google-cloud-functions/tree-sitter-service/**"
# Runs: parsing tests for all 10+ supported languages
```

Change the Chrome extension? Only relevant tests run. Update the backend? Backend tests plus any integration tests that depend on it.

### The CLAUDE.md Convention

Every major directory has a CLAUDE.md file that documents:

* What this code does
* Tech stack and versions
* Quick start commands
* Architecture decisions
* Common patterns

```
CLAUDE.md                          # Root-level overview
├── frontend/CLAUDE.md            # Next.js 15, React 19, Tailwind v4
├── backend/CLAUDE.md             # Cloudflare Workers, Hono, Mastra
├── external/chrome-extension/CLAUDE.md
├── external/google-cloud-functions/CLAUDE.md
└── marketing/email/CLAUDE.md     # MJML email guidelines
```

This isn't just for humans—AI coding assistants read these files. When Claude Code works on our frontend, it reads `frontend/CLAUDE.md` and knows we're using Next.js 15 with React 19, npm (not pnpm), and specific patterns.

### Consistent Tooling

One configuration, everywhere:

```
.prettierrc              # Formatting (all JS/TS)
.eslintrc               # Linting (shared rules)
tsconfig.json           # TypeScript base config
```

New developer? `npm install` in the directory you're working on. Everything works.

---

The Challenges (And How We Handle Them)
---------------------------------------

### Challenge: Repository Size

**Why it's not a problem (yet):**

* Clone time: ~20 seconds
* Git operations: still snappy
* We haven't needed sparse checkout, LFS, or shallow clones

**When we might need to:**

* Large binary assets would go to R2/S3, not git
* If we hit 1GB+, we'd look at shallow clones for CI
* Truly independent services could be extracted

### Challenge: Build Times

**Problem**: If everything is connected, does everything rebuild?

**Reality**: No. Each project builds independently:

```
# Frontend build (only rebuilds frontend)
cd frontend && npm run build

# Backend build (only rebuilds backend)
cd backend && npm run build

# Extension build (only rebuilds extension)
cd external/chrome-extension && npm run build
```

We use Turbopack for frontend dev (fast HMR), Wrangler for backend dev (fast reload), and WXT for extension dev (fast rebuild).

### Challenge: Permission Boundaries

**Problem**: Not everyone should see everything.

**Our situation**: We're a small team. Everyone can see everything. That's a feature, not a bug—it enables cross-pollination.

**If we grew and needed boundaries:**

* GitHub CODEOWNERS for review requirements
* Branch protection rules
* Potentially split truly sensitive codebases (but we'd resist this)

### Challenge: Context Switching

**Problem**: Jumping between TypeScript (frontend), TypeScript (backend), Apps Script (Google add-on), and MJML (emails) feels disorienting.

**Solutions:**

* Consistent patterns across projects (same linting, same formatting)
* CLAUDE.md files explain context immediately
* IDE workspace configurations

---

Conclusion
----------

Our monorepo isn't about following a trend. It's about removing friction between things that naturally belong together, something that is critical when related context is everything.

When a feature touches the backend API, the frontend component, the documentation, and the marketing site—why should that be four repositories, four PRs, four merge coordination meetings?

The monorepo isn't a constraint. It's a force multiplier.

---

*Kasava is built as a unified platform. [See what we've built](https://kasava.dev)*
