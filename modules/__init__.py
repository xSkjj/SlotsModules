from configparser import ConfigParser

config = ConfigParser()

config.read(".\\settings.ini") # get window settings from settings.ini


bgSlots = config.get ("customisation", "slots_background")
bgColor = config.get ("customisation", "window_background")
symColor = config.get("customisation", "symbol_color")

slotAmount = config.getint("game_settings", "slot_amount")
slotAmt = slotAmount if slotAmount > 1 and slotAmount <= 7 else 2 if slotAmount < 2 else 7

bal = 1000
symbols = "🍐🍒💲💰🍌🍀🍋♥♦♣♠🌞🍇🍊🍉🔔𝟕🍸"
