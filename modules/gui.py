import tkinter as tk
from random import randint
from modules import bgColor, bgSlots, slotAmt, symData, symbols, startBal, fastSpin, spin, utility
from classes import slot, colorbutton, settings

root = tk.Tk()

# apply window settings
root.iconbitmap(".\\assets\\icon.ico")  # set the icon in the top left of the window
root.title("Slots")  # set window title of the title bar
root.resizable(False, False)  # disable resizability in x and y
root.minsize(480, 480)  # set minimum width and height of the window
root["background"] = bgColor  # set the background color of the window

# define elements and set their properties
header = tk.Label(root,  # "SLOTS" title
                  text="$  L  O  T  $",
                  font="Impact 48",
                  fg="gold",
                  bg=bgColor)

slotCanvas = tk.Canvas(root,  # canvas in which the slots are displayed in
                       width=slotAmt * 120,
                       height=120,
                       bg=bgSlots,
                       highlightthickness=0)

output = tk.Label(root,  # Label for various text strings to tell the user something
                  text="How many credits would you like to use?",
                  font="Consolas 14",
                  fg="#41ff00",
                  bg="black")

userInputs = tk.Frame(root,  # a set of widgets for user interaction
                      bg=bgColor)

amtInputLabel = tk.Label(userInputs,  # Label for the input field for the balance amount the user wants to use
                         text="Amount:",
                         font="Arial 16 bold",
                         fg="white",
                         bg=bgColor)

amtInput = tk.Entry(userInputs,  # an input field where the user chooses an amount
                    # this is where bugs and errors may happen
                    textvariable=tk.StringVar(value=1),
                    font="Consolas 16",
                    fg="white",
                    bg="#404040",
                    insertbackground="white",
                    relief="flat")

spinBtn = colorbutton.ColorButton(userInputs, "green",  # the button to start the spinning
                                  command=spin.spin,
                                  text="spin",
                                  font="Arial 20 bold")

balLabel = tk.Label(root,  # the Label to display the current user balance
                    text=f"Balance: {startBal}",
                    font="Arial 16 bold",
                    fg="gold",
                    bg=bgColor)

settingsBtn = colorbutton.ColorButton(root, "grey",
                                      command=utility.show_settings,
                                      text="⚙",
                                      font="Arial 20")

settingsFrame = tk.Frame(root,  # the container for all settings
                         bg=bgColor,
                         highlightthickness=4,
                         highlightbackground="white")

settingsLabel = tk.Label(settingsFrame,
                         text="SETTINGS",
                         font="Impact 48",
                         fg="white",
                         bg=bgColor)
settingsLabel.pack()

customisationSettings = settings.Section(settingsFrame,
                                         text="Customisation")

bgColorSetting = settings.Section(customisationSettings,
                                  text="Background color",
                                  grid=True)
bgColorPicker = tk.Button(bgColorSetting,
                          text="pick",
                          bg=bgColor,
                          command=lambda: utility.change_color(bgColorPicker, "window_background"),
                          font="Arial 10 bold")

bgSlotsSetting = settings.Section(customisationSettings,
                                  text="Slots background",
                                  grid=True)
bgSlotsPicker = tk.Button(bgSlotsSetting,
                          text="pick",
                          bg=bgSlots,
                          command=lambda: utility.change_color(bgSlotsPicker, "slots_background"),
                          font="Arial 10 bold")

gameSettings = settings.Section(settingsFrame,
                                text="Game Settings")

slotAmtSetting = settings.Section(gameSettings,
                                  text="Slot amount",
                                  grid=True)

fastSpinSetting = settings.Section(gameSettings,
                                   text="  Fast spin",
                                   grid=True)

check = tk.BooleanVar(value=fastSpin)
fastSpinCheck = tk.Checkbutton(fastSpinSetting,
                               var=check,
                               bg=bgColor,
                               activeforeground="white",
                               activebackground=bgColor)

closeSettingsBtn = colorbutton.ColorButton(settingsFrame, "grey",
                                           command=utility.hide_settings,
                                           text="✕",
                                           font="Arial 20")

sym = {}  # dictionary for each slot
for i in range(slotAmt):  # has to be in a for loop, since the user can change the amount of slots
    sym[i] = slot.Slot(slotCanvas, i)
    randSym = symbols[randint(0, len(symbols) - 1)]
    sym[i].set(sym[i].symbol,
               text=randSym,
               fill=symData[randSym]["color"])
