"""
The **Holiday Countdown Board** displays upcoming holidays on an LED matrix with customizable colors and images.
"""
import json
from pathlib import Path

# Load plugin metadata
_plugin_dir = Path(__file__).parent
with open(_plugin_dir / "plugin.json") as f:
    _metadata = json.load(f)

# Expose metadata as module variables (backward compatibility)
__plugin_id__ = _metadata["name"]
__version__ = _metadata["version"]
__description__ = _metadata["description"]
__board_name__ = _metadata["description"]
__author__ = _metadata.get("author", "")
__requirements__ = _metadata.get("requirements", {}).get("python_dependencies", [])
__min_app_version__ = _metadata.get("requirements", {}).get("app_version", "")
__preserve_files__ = _metadata.get("preserve_files", [])
