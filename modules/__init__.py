from configparser import ConfigParser

config = ConfigParser()

config.read(".\\settings.ini") # get window settings from settings.ini


bgSlots = config.get ("customisation", "slots_background")
bgColor = config.get ("customisation", "window_background")

slotAmount = config.getint("game_settings", "slot_amount")
minSlots = 2
maxSlots = 7
slotAmt = minSlots if slotAmount < minSlots else maxSlots if slotAmount > maxSlots else slotAmount

bal = 1000
# symData = { symbol: { symbol color: color, *slotAmount: multiplier}}
symData = {
    "🍒": {"color": "#790604", 2: 0, 3: 1},
    "🍇": {"color": "#6f2da8", 2: 0, 3: 1},
    "🍋": {"color": "#fff44f", 2: 1, 3: 3},
    "🍊": {"color": "#ffa500", 2: 1, 3: 3},

    "♥": {"color": "brown", 2: 2, 3: 10},
    "♦": {"color": "brown", 2: 2, 3: 10},
    "♣": {"color": "#101010", 2: 2, 3: 10},
    "♠": {"color": "#101010", 2: 2, 3: 10},

    "💰": {"color": "#a76222", 2: 5, 3: 30},
    "🔔": {"color": "#f6b800", 2: 5, 3: 30},
    "🍀": {"color": "#92b832", 2: 5, 3: 30},
    "🌞": {"color": "#ffcd35", 2: 5, 3: 30},

    "𝟕": {"color": "brown", 2: 10, 3: 200}
}

symbols = [key for key in symData]
