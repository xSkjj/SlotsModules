from configparser import ConfigParser

config = ConfigParser()

config.read(".\\settings.ini") # get window settings from settings.ini


bgSlots = config.get ("customisation", "slots_background")
bgColor = config.get ("customisation", "window_background")
slotFont = config.get("customisation", "slots_font")

slotCols = config.getint("game_settings", "slot_columns")
slotRows = config.getint("game_settings", "slot_rows")

bal = 1000
