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