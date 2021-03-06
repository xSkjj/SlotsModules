from configparser import ConfigParser

config = configQ = ConfigParser()
config.read("settings.ini")  # get window settings from settings.ini

config.bgColor = config.get("customisation", "background_color")
config.bgSlots = config.get("customisation", "slots_background")

config.slotAmt = config.getint("game_settings", "slot_amount")
config.fastSpin = config.getboolean("game_settings", "fast_spin")

startBalance = 1000

symData = {
    "🍒": {"color": "#790604", "occurrence": 15},
    "🍇": {"color": "#6f2da8", "occurrence": 15},
    "🍋": {"color": "#fff44f", "occurrence": 15},
    "🍊": {"color": "#ffa500", "occurrence": 15},

    "♥": {"color": "brown", "occurrence": 5},
    "♦": {"color": "brown", "occurrence": 5},
    "♣": {"color": "#101010", "occurrence": 5},
    "♠": {"color": "#101010", "occurrence": 5},

    "💰": {"color": "#a76222", "occurrence": 2},
    "🔔": {"color": "#f6b800", "occurrence": 2},
    "🍀": {"color": "#92b832", "occurrence": 2},
    "🌞": {"color": "#ffcd35", "occurrence": 2},

    "𝟕": {"color": "brown", "occurrence": 1}
}

symbols = [key for key in symData for i in range(symData[key]["occurrence"])]
