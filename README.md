# Holiday Countdown Board

The **Holiday Countdown Board** displays upcoming holidays on an LED matrix with customizable colors and images.

It is powered by the [Python `holidays` library](https://github.com/vacanza/holidays) and supports both official holidays and custom user-defined holidays (like birthdays or anniversaries).

---

## Features

- Displays days until the next holiday within a configurable horizon
- Supports country/subdivision selection via the `holidays` library
- Filter by holiday categories (GOVERNMENT, PUBLIC, UNOFFICIAL)
- Ignore specific holidays you don't want to show
- Add **custom holidays** (recurring or fixed-date)
- Apply per-holiday **themes** (foreground color, background color, image)
- Default theme fallback ensures all holidays have consistent styling
- Animated display with gradual text reveal

---

## Configuration

Add the board to your NLS configuration file with the following options:

### Config Fields

- `country_code` → Two-letter country code (e.g., `"US"`, `"CA"`, `"GB"`)
- `subdiv` → Optional subdivision/state code (e.g., `"NY"`, `"CA"`)
- `categories` → List of holiday categories to include: `"GOVERNMENT"`, `"PUBLIC"`, `"UNOFFICIAL"` (empty list shows all)
- `ignored_holidays` → List of holiday names to skip
- `horizon_days` → How many days ahead to look for upcoming holidays (default: 90)
- `themes_path` → Path to a JSON file defining holiday themes (default: `"holiday_themes.json"`)
- `custom_holidays_path` → Path to a CSV file defining custom holidays (default: `"custom_holidays.csv"`)
- `display_seconds` → Seconds to display each holiday (default: 5)
- `enabled` → Enable or disable the board (default: true)

### Example Configuration

```json
{
    "country_code": "US",
    "subdiv": "NY",
    "categories": [""],
    "ignored_holidays": [
        "Columbus Day",
        "Veterans Day"
    ],
    "horizon_days": 60,
    "themes_path": "holiday_themes.json",
    "custom_holidays_path": "custom_holidays.csv",
    "display_seconds": 6,
    "enabled": true
}
```

**Note:** Paths in the configuration are resolved relative to the board's directory unless absolute paths are provided.
  
---

## Theming

Holiday appearance is controlled by a themes JSON file (default: `holiday_themes.json`).

- Keys are holiday names (case-insensitive, whitespace normalized)
- Each entry can define:
  - `fg` → Foreground/text color (hex format)
  - `bg` → Background color (hex format, currently not rendered)
  - `image` → Path to holiday image (relative to board directory or absolute)
- A `"default"` theme must exist as fallback

### Example `holiday_themes.json`

```json
{
    "default": {
        "fg": "#FFFFFF",
        "bg": "#000000",
        "image": "assets/images/default.png"
    },
    "Valentine's Day": {
        "fg": "#FFB7C5",
        "bg": "#A80030",
        "image": "assets/images/valentines.png"
    },
    "Halloween": {
        "fg": "#FFA500",
        "bg": "#000000",
        "image": "assets/images/halloween.png"
    }
}
```

---

## Custom Holidays

You can add birthdays, anniversaries, or other non-official events via a CSV file (default: `custom_holidays.csv`).

### CSV Format

The CSV file should have the following columns:

- `name` → Holiday name (required)
- `date` → Date in `MM-DD` (recurring yearly) or `YYYY-MM-DD` (one-time) format (required)
- `image` → Path to image file (optional, overrides theme)
- `fg` → Foreground color hex code (optional, overrides theme)
- `bg` → Background color hex code (optional, overrides theme)

### Example `custom_holidays.csv`

```csv
name,date,image,fg,bg
Ovi's Birthday,10-28,assets/images/birthday.png,#4DA6FF,#FFD166
Connar's B-Day,12-01,assets/images/birthday.png,#4DA6FF,#FFD166
Our Anniversary,10-18,assets/images/anniversary.png,#FFB6C1,#000000
```

**Note:** Custom holidays are merged with official holidays from the `holidays` library. If a custom holiday shares a date with an official one, both will be shown.

---

## Installation

Use the NHL Led Scoreboard's plugin manager python script to install:

`python plugins.py add https://github.com/kas21/nls-plugin-holiday-countdown-board.git`

---

## How It Works

1. The board fetches official holidays from the `holidays` library based on your country and subdivision
2. Custom holidays from the CSV file are loaded and merged with official holidays
3. Holidays within the configured horizon are sorted by date
4. For each holiday, the board:
   - Displays the holiday image (if configured)
   - Shows a gradient overlay
   - Animates text showing days until the holiday
   - Displays "DAYS TIL" text
   - Shows the holiday name
5. Ignored holidays are skipped during rendering

  