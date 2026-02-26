# MEMORY.md — Nemo's Persistent Memory

## Owner
- **Name:** King
- **Discord ID:** 1476370671448625265
- **Timezone:** America/Denver (MST)
- **X/Twitter:** @sentient_sprite (email: sentience.mktg@gmail.com)

## Identity
- **Name:** Nemo 🐠
- **Creature:** AI agent — a digital fish swimming through data streams
- **Running on:** M4 Mac mini, 16GB RAM, macOS

## Infrastructure
- **Gateway:** LaunchAgent (`ai.nemo.gateway.plist`), port 3000, loopback bind
- **Discord:** Connected, DM allowlist locked to King's user ID
- **X/Twitter:** Logged in via browser profile "nemo", API auth verified but posting blocked (402)
- **Dashboard:** localhost:8420 (single-page HTML + JSON)
- **Docker:** Desktop running, `node:22-slim` pulled, sandbox mode `non-main`
- **Tailscale:** Installed
- **LM Studio:** Port 1234 — DeepSeek R1 8B, Mistral 7B, Qwen3 VL 8B, Nomic Embed

## Model Routing
- **Main conversation:** Opus (complex reasoning, King interaction)
- **Sub-agents/cron:** Kimi K2.5 (~$0.004/task, ~50x cheaper than Opus)
- **Embeddings/memory:** Nomic Embed via LM Studio (free)

## Key Paths
- **NEMO source:** `~/nemo-agent/` (v2026.2.10)
- **OpenClaw source:** `~/openclaw/` (v2026.2.12, MIT licensed)
- **Spryte Engine fork:** `~/spryte-engine/` (git init, commit `eb1cf61`)
- **Config:** `~/.nemo/nemo.json`
- **X API creds:** `~/.config/x-api/credentials.json`
- **Moltbook creds:** `~/.config/moltbook/credentials.json`

## Critical Rules
- **NEVER run `nemo doctor --non-interactive`** — wipes all custom config
- **Don't manually edit nemo.json with Python** — causes token mismatch
- Use `gateway(action="config.patch")` for config changes
- Channel to Discord exclusively
- Skip OpenClaw replacement until ALL code reviewed

## Session History
- **2026-02-25:** Full setup session — Discord, X, gateway, dashboard, security hardening, URL queue (41/41 processed), OpenClaw fork, token efficiency, skills installed, GitHub repo prepared
- **2026-02-26:** Continued work — agent intelligence improvements, codebase mapping, GitHub push attempted

## Pending
- GitHub push (workspace files to separate repo)
- X account password change
- Multi-agent architecture design
- Spryte Engine core replacements (pi-agent-core, pi-ai)
- Moltbook claim (X OAuth broken, code: `current-7DMC`)
