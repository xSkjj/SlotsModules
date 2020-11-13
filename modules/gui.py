import tkinter as tk
from random import randint
from modules import bgColor, bgSlots, slotAmt, symData, symbols, bal, func
from classes import slot

root = tk.Tk()

icon = ".\\assets\\icon.ico" # icon  for the window
title = "Slots"              # title for the window

# apply window settings
root.iconbitmap(icon)        # set the icon in the top left of the window
root.title(title)            # set window title of the title bar
root.resizable(False, False) # disable resizability in x and y
root["background"] = bgColor # set the background of the window


# make elements and set their properties
header = tk.Label(root, # vvv "SLOTS" title
                  text = "$  L  O  T  $",
                  font = "Impact 24",
                  fg   = "gold",
                  bg   = bgColor)

slotCanvas = tk.Canvas(root, # canvas in which the slots are displayed in
                       width              = slotAmt * 100,
                       height             = 100,
                       bg                 = bgSlots,
                       highlightthickness = 0)

output = tk.Label(root, # Label for various text strings to tell the user something
                  text = "How many credits would you like to use?",
                  font = "Consolas 10 bold",
                  fg   = "white",
                  bg   = "black")

userInputs = tk.Frame(root, # a set of widgets for user interaction
                      bg = bgColor)

amtInputLabel = tk.Label(userInputs, # Label for the input field for the balance amount the user wants to use
                         text = "Amount:",
                         font = "Arial 10 bold",
                         fg   = "white",
                         bg   = bgColor)

amtInput = tk.Entry(userInputs, # an input field where the user chooses an amount; this is where bugs and errors may happen
                    textvariable     = tk.StringVar(value=0),
                    fg               = "white",
                    bg               = "#404040",
                    insertbackground = "white",
                    relief           = "flat")

spinBtn = tk.Button(userInputs, # the button to start the spining; it's where the magic happens
                    command= func.trySpin,
                    text   = "spin",
                    font   = "Arial 10 bold",
                    fg     = "#050",
                    activeforeground = "#030",
                    bg     = "#7c7",
                    activebackground = "#5a5",
                    relief = "flat")

balLabel = tk.Label(root, # the Label to display the current user balance
                    text = f"Balance: {bal}",
                    font = "Arial 10 bold",
                    fg   = "gold",
                    bg   = bgColor)

sym = {} # dictionary for each slot
for i in range(slotAmt): # has to be in a for loop, since the user can change the amount of slots
    sym[i] = slot.Slot(slotCanvas, i)
    randSym = symbols[randint(0, len(symbols)-1)]
    sym[i].set(sym[i].symbol,
               text = randSym,
               fill = symData[randSym]["color"])
