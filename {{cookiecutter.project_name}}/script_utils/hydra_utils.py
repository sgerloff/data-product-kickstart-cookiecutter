import re

from typing import List


def parse_overrides(overrides: List[str]) -> dict:
    _override_dict = {}
    for override in overrides:
        key, value = override.split("=")
        key = re.sub(r"[^a-zA-Z0-9._\-/ ]", "", key)
        _override_dict[key] = value
    return _override_dict
