import os
import json
from pathlib import Path
from typing import Any, Dict, List

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
HISTORY_DIR = DATA_DIR / "history"
USERS_FILE = DATA_DIR / "users.json"


def ensure_data_dirs() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)


def get_history_filepath(user_id: str) -> Path:
    ensure_data_dirs()
    return HISTORY_DIR / f"history_{user_id}.json"


def get_summary_filepath(user_id: str) -> Path:
    ensure_data_dirs()
    return DATA_DIR / f"summary{user_id}.json"


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: Any) -> None:
    ensure_data_dirs()
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_history(user_id: str) -> List[Dict[str, Any]]:
    return load_json(get_history_filepath(user_id), default=[])


def save_history(user_id: str, history: List[Dict[str, Any]]) -> None:
    write_json(get_history_filepath(user_id), history)


def load_summary(user_id: str) -> Dict[str, Any]:
    return load_json(get_summary_filepath(user_id), default=None)


def load_users() -> List[Dict[str, Any]]:
    if not USERS_FILE.exists():
        raise FileNotFoundError("Users file not found")
    return load_json(USERS_FILE, default=[])
