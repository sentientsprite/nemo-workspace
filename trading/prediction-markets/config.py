"""
Configuration for prediction market copy-trading bot.
All settings loaded from environment variables with sensible defaults.
"""

import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class KalshiConfig:
    email: str = os.getenv("KALSHI_EMAIL", "")
    password: str = os.getenv("KALSHI_PASSWORD", "")
    api_key: str = os.getenv("KALSHI_API_KEY", "")
    api_secret: str = os.getenv("KALSHI_API_SECRET", "")
    base_url: str = os.getenv(
        "KALSHI_BASE_URL", "https://trading-api.kalshi.com/trade-api/v2"
    )
    demo: bool = os.getenv("KALSHI_DEMO", "false").lower() == "true"

    def __post_init__(self):
        if self.demo:
            self.base_url = "https://demo-api.kalshi.co/trade-api/v2"


@dataclass
class PolymarketConfig:
    private_key: str = os.getenv("POLYMARKET_PRIVATE_KEY", "")
    api_key: str = os.getenv("POLYMARKET_API_KEY", "")
    api_secret: str = os.getenv("POLYMARKET_API_SECRET", "")
    api_passphrase: str = os.getenv("POLYMARKET_API_PASSPHRASE", "")
    chain_id: int = int(os.getenv("POLYMARKET_CHAIN_ID", "137"))  # Polygon mainnet
    funder: str = os.getenv("POLYMARKET_FUNDER", "")


@dataclass
class RiskConfig:
    max_per_market_pct: float = float(os.getenv("RISK_MAX_PER_MARKET_PCT", "0.10"))
    max_total_exposure_pct: float = float(os.getenv("RISK_MAX_TOTAL_EXPOSURE_PCT", "0.30"))
    daily_loss_limit_pct: float = float(os.getenv("RISK_DAILY_LOSS_LIMIT_PCT", "0.15"))
    min_leader_winrate: float = float(os.getenv("RISK_MIN_LEADER_WINRATE", "0.50"))
    leader_winrate_window: int = int(os.getenv("RISK_LEADER_WINRATE_WINDOW", "20"))
    max_positions_per_leader: int = int(os.getenv("RISK_MAX_POSITIONS_PER_LEADER", "3"))


@dataclass
class Config:
    # Platform selection
    platform: str = os.getenv("PLATFORM", "kalshi")  # kalshi | polymarket
    dry_run: bool = os.getenv("DRY_RUN", "true").lower() == "true"

    # Copy trading params
    copy_delay_seconds: float = float(os.getenv("COPY_DELAY_SECONDS", "5.0"))
    sizing_ratio: float = float(os.getenv("SIZING_RATIO", "1.0"))  # multiplier on proportional sizing
    poll_interval_seconds: int = int(os.getenv("POLL_INTERVAL_SECONDS", "30"))
    bankroll: float = float(os.getenv("BANKROLL", "100.0"))  # USD

    # Leader addresses / IDs to follow
    kalshi_leader_ids: list[str] = field(default_factory=lambda: _parse_list("KALSHI_LEADER_IDS"))
    polymarket_leader_addresses: list[str] = field(default_factory=lambda: _parse_list("POLYMARKET_LEADER_ADDRESSES"))

    # Webhook
    webhook_port: int = int(os.getenv("WEBHOOK_PORT", "5088"))
    webhook_secret: str = os.getenv("WEBHOOK_SECRET", "")

    # Sub-configs
    kalshi: KalshiConfig = field(default_factory=KalshiConfig)
    polymarket: PolymarketConfig = field(default_factory=PolymarketConfig)
    risk: RiskConfig = field(default_factory=RiskConfig)

    # Data
    data_dir: str = os.getenv("DATA_DIR", "data")
    trades_file: str = os.getenv("TRADES_FILE", "data/trades.jsonl")


def _parse_list(env_var: str) -> list[str]:
    """Parse comma-separated env var into list."""
    raw = os.getenv(env_var, "")
    if not raw.strip():
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]


# Singleton
cfg = Config()
