# 🐠 Nemo Workspace

Agent configuration, dashboard, memory, and references for [Nemo](https://github.com/sentientsprite/nemo-agent) — an AI agent running 24/7 on a Mac mini.

## Structure

```
├── AGENTS.md           # Agent guidelines and behavior rules
├── SOUL.md             # Personality and identity
├── IDENTITY.md         # Who Nemo is
├── USER.md             # About the human (King)
├── MEMORY.md           # Persistent memory
├── TOKEN-EFFICIENCY.md # Cost optimization and model routing
├── HEARTBEAT.md        # Periodic check triggers
├── TOOLS.md            # Local tool notes
├── dashboard/          # Web dashboard (localhost:8420)
├── memory/             # Daily session logs
└── references/         # Research and strategy docs
```

## Dashboard

Serve locally:
```bash
cd dashboard && python3 -m http.server 8420
```

## Agent

Running on NEMO (nemo-agent) with:
- **Main model:** Claude Opus (complex reasoning)
- **Sub-agents:** Kimi K2.5 (~$0.004/task)
- **Embeddings:** Nomic Embed via LM Studio (free)
- **Channel:** Discord (DM only)
