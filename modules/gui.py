import tkinter as tk
from random import randint
from modules import bgColor, bgSlots, slotFont, slotAmt, bal, symbols, spin


root = tk.Tk()

icon = ".\\assets\\icon.ico"
title = "Slots"

# apply window settings
root.iconbitmap(icon)
root.title(title)
root.resizable(False, False)
root["background"] = bgColor


# make elements and set their properties
header = tk.Label(root,
                  text = "$  L  O  T  $",
                  font = "Impact 24",
                  fg   = "gold",
                  bg   = bgColor)

slotsDisplay = tk.Canvas(root,
                         width              = slotAmt * 100,
                         height             = 100,
                         bg                 = "white",
                         highlightthickness = 0)
for slot in range(slotAmt):
    slotsDisplay.create_rectangle(slot*100+1, 1,
                                  slot*100+98, 98,
                                  outline = "white",
                                  fill    = bgSlots)
    slotsDisplay.create_text(slot*100+50, 50,
                             text = symbols[randint(0, len(symbols) - 1)],
                             font = (slotFont, 48, "bold"),
                             fill = "white",
                             tags = f"sym{slot}")

output = tk.Label(root,
                  text = "How many credits would you like to use?",
                  font = "Consolas 10 bold",
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
                    textvariable     = "0",
                    fg               = "white",
                    bg               = "#404040",
                    insertbackground = "white",
                    relief           = "flat")

spinBtn = tk.Button(userInputs,
                    command= spin.trySpin,
                    text   = "spin",
                    font   = "Arial 10 bold",
                    fg     = "#050",
                    bg     = "light green",
                    relief = "flat")

balLabel = tk.Label(root,
                    text = f"Balance: {bal}",
                    font = "Arial 10 bold",
                    fg   = "gold",
                    bg   = bgColor)
