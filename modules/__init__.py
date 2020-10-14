from modules import gui
from configparser import ConfigParser
config = ConfigParser()

config.read(".\\settings.ini") # get window settings from settings.ini

icon = config.get("window_settings", "icon")
title = config.get("window_settings", "title")

minWidth = config.getint("window_settings", "minWidth")
minHeight = config.getint("window_settings", "minHeight")
maxWidth = config.getint("window_settings", "maxWidth")
maxHeight = config.getint("window_settings", "maxHeight")

windowWidth = config.get("window_settings", "windowWidth")
windowHeight = config.get("window_settings", "windowHeight")
offsetx = config.get("window_settings", "offsetx")
offsety = config.get("window_settings", "offsety")


# apply window settings
root = gui.root
root.iconbitmap(icon)
root.title(title)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)
root.geometry((windowWidth + "x" + windowHeight + "+" + offsetx + "+" + offsety))
