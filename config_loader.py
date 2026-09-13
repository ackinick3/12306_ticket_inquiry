import json
from pathlib import Path


def load_headers(config_path="config.json"):
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    required_keys = ("cookie", "user_agent")
    missing_keys = [key for key in required_keys if not config.get(key)]
    if missing_keys:
        raise ValueError(f"配置文件缺少必填项: {', '.join(missing_keys)}")

    return {
        "Cookie": config["cookie"],
        "User-Agent": config["user_agent"],
    }
