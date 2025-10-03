"""
The **Holiday Countdown Board** displays upcoming holidays on an LED matrix with customizable colors and images.
"""

# Board metadata using standard Python package conventions
__plugin_id__ = "holiday_countdown_board"  # Canonical folder name for installation
__version__ = "2025.09.01"
__description__ = "Holiday Countdown Board displays upcoming holidays with customizable themes"
__board_name__ = "Holiday Countdown Board"
__author__ = "kas"

# Board requirements
__requirements__ = [
    "pillow",
    "holidays"
]

# Minimum application version required
__min_app_version__ = "2025.09.00"

# Files to preserve during plugin updates/removals (optional)
# The plugin manager will preserve these files when updating or removing with --keep-config
# Supports glob patterns like *.csv, data/*, custom_*
# Default if not specified: ["config.json", "*.csv", "data/*", "custom_*"]
__preserve_files__ = [
    "config.json",
    "image_offsets.json",
    "custom_holidays.csv",
    # Add other user-modifiable files here, e.g.:
    # "custom_data.csv",
    # "data/*.json",
]
