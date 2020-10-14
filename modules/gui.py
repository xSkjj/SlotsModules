import tkinter as tk
from modules import spin

from configparser import ConfigParser
config = ConfigParser()
config.read(".\\settings.ini")
bgColor = config.get("window_settings", "bgColor")


root = tk.Tk()
root["background"] = bgColor

# make elements and set their properties
header = tk.Label(root,
                  text = "$  L  O  T  $",
                  font = "Impact 24",
                  fg   = "gold",
                  bg   = bgColor)

slotsDisplay = tk.Canvas(root,
                         width              = 300,
                         height             = 100,
                         bg                 = "white",
                         highlightthickness = 0)
slotsDisplay.create_rectangle(1,   1,  98, 98, outline="white", fill="#c3a469")
slotsDisplay.create_rectangle(101, 1, 198, 98, outline="white", fill="#c3a469")
slotsDisplay.create_rectangle(201, 1, 298, 98, outline="white", fill="#c3a469")
slotsDisplay.create_text(50,  50, text="$", font="Consolas 32", fill="white", tags="symA")
slotsDisplay.create_text(150, 50, text="$", font="Consolas 32", fill="white", tags="symB")
slotsDisplay.create_text(250, 50, text="$", font="Consolas 32", fill="white", tags="symC")

output = tk.Label(root,
                  text = "How much credits would you like to use?",
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
                    text  = 0,
                    fg    = "white",
                    bg    = "#404040",
                    insertbackground="#bee",
                    relief= "flat")

spinBtn = tk.Button(userInputs,
                    command= spin.trySpin,
                    text   = "spin",
                    font   = "Arial 10 bold",
                    fg     = "#050",
                    bg     = "light green",
                    relief = "flat")

balLabel = tk.Label(root,
                    text = f"Balance: {spin.bal}",
                    font = "Arial 10 bold",
                    fg   = "gold",
                    bg   = bgColor)
