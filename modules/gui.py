import tkinter as tk
from random import randint
from modules import bgColor, bgSlots, symColor, slotAmt, bal, symbols, func
from classes import slot

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

slotCanvas = tk.Canvas(root,
                       width              = slotAmt * 100,
                       height             = 100,
                       bg                 = bgSlots,
                       highlightthickness = 0)

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
                    textvariable     = tk.StringVar(value=0),
                    fg               = "white",
                    bg               = "#404040",
                    insertbackground = "white",
                    relief           = "flat")

spinBtn = tk.Button(userInputs,
                    command= func.trySpin,
                    text   = "spin",
                    font   = "Arial 10 bold",
                    fg     = "#050",
                    activeforeground = "#030",
                    bg     = "#7c7",
                    activebackground = "#5a5",
                    relief = "flat")

balLabel = tk.Label(root,
                    text = f"Balance: {bal}",
                    font = "Arial 10 bold",
                    fg   = "gold",
                    bg   = bgColor)

for i in range(slotAmt):
    slot.Slot(slotCanvas, i)
