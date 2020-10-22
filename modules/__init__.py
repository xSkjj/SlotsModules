from configparser import ConfigParser

config = ConfigParser()

config.read(".\\settings.ini") # get window settings from settings.ini


bgSlots = config.get ("customisation", "slots_background")
bgColor = config.get ("customisation", "window_background")
slotFont = config.get("customisation", "slots_font")

slotAmount = config.getint("game_settings", "slot_amount")
slotAmt = slotAmount if slotAmount > 1 and slotAmount < 7 else 2 if slotAmount < 2 else 6

bal = 1000
symbols = "!$&?#☺♥♦♣♠★♂♀♪♫7"
