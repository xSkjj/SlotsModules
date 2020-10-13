import tkinter as tk

# window settings
icon = r".\assets\icon.ico" # window icon
title = "Slots"             # window title
minWidth = 400              # minimum resize width
minHeight = 255             # minimum resize height
maxWidth = 400              # maximum resize width
maxHeight = 255             # maximum resize height
windowWidth = "400"         # starting width
windowHeight = "255"        # starting height
offsetx = "200"             # left border offset
offsety = "200"             # top border offset
bgColor = "#202020"         # window background color

# apply window settings
root = tk.Tk()
root.iconbitmap(icon)
root.title(title)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)
root.geometry((windowWidth + "x" + windowHeight + "+" + offsetx + "+" + offsety))
root["background"] = bgColor

# make elements and set their properties
header = tk.Label(root,
                  text = "S  L  O  T  S",
                  font = "Impact 24",
                  fg   = "gold",
                  bg   = bgColor)

slotsDisplay = tk.Canvas(root,
                         width              = 300,
                         height             = 100,
                         bg                 = "#c3a469",
                         highlightthickness = 0)
slotsDisplay.create_rectangle(0,   0,  99, 99, outline="white")
slotsDisplay.create_rectangle(100, 0, 199, 99, outline="white")
slotsDisplay.create_rectangle(200, 0, 299, 99, outline="white")
slotsDisplay.create_text(50,  50, text="$", font="Consolas 32", fill="white", tags="symA")
slotsDisplay.create_text(150, 50, text="$", font="Consolas 32", fill="white", tags="symB")
slotsDisplay.create_text(250, 50, text="$", font="Consolas 32", fill="white", tags="symC")

output = tk.Label(root,
                  text = "How much credits would you like to use?",
                  font = "Arial 10 bold",
                  fg   = "white",
                  bg   = "black")

userInputs = tk.Frame(root,
                      bg = bgColor)

amtInputLabel = tk.Label(userInputs,
                         text = "Amount:",
                         font = "Arial 10 bold",
                         fg   = "white",
                         bg   = bgColor)

amtInput = tk.Entry(userInputs,
                    bg               = "#404040",
                    insertbackground = "white",
                    fg               = "white",
                    relief           = "flat")

spinBtn = tk.Button(userInputs,
                    command = None,
                    text    = "spin",
                    font    = "Arial 10 bold",
                    fg      = "#050",
                    bg      = "light green",
                    relief  = "flat")

balLabel = tk.Label(root,
                    text = "Balance: ",
                    font = "Arial 10 bold",
                    fg   = "gold",
                    bg   = bgColor)
