# MEMORY.md

## Infrastructure & Configuration

**Hardware**: M4 Mac Mini in USA (usually connected to Canadian VPN)

**Critical Constraint**: Moonshot/Kimi API returns 401 invalid authentication from Canadian IPs — do NOT attempt to use moonshot or kimi models. They will never work from this location.

**Primary Model**: anthropic/claude-opus-4-1-20250805 (Anthropic works fine)

**Local Inference**: 
- LM Studio at http://192.168.1.119:1234
- Model loaded: qwen3.5-9b
- Use as secondary only when context requirements are under 16,000 tokens

**Authentication**: 
- Credentials stored at `~/.nemo/agents/main/agent/auth-profiles.json`
- **This is the only file that matters** for authentication — not nemo.json or .env

**Status**: Recently recovered from credit issues (2025-01-16)
