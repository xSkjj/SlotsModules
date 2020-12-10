import tkinter as tk
import skinter as sk
from random import randint
from misc import bgColor, bgSlots, slotAmt, symData, symbols, startBal, fastSpin, spin, utility
from classes import slot

root = tk.Tk()

# apply window settings
root.iconbitmap(".\\assets\\icon.ico")  # set the icon in the top left of the window
root.title("Slots")  # set window title of the title bar
root.resizable(False, False)  # disable resizability in x and y
root.minsize(480, 480)  # set minimum width and height of the window
root["bg"] = bgColor  # set the background color of the window

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
                  bg="#101010")

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

spinBtn = sk.Button(userInputs, "#77cc77",  # the button to start the spinning
                    command=spin.spin,
                    text="spin",
                    font="Arial 20 bold")

balLabel = tk.Label(root,  # the Label to display the current user balance
                    text=f"Balance: {startBal}",
                    font="Arial 16 bold",
                    fg="gold",
                    bg=bgColor)

settingsBtn = sk.Button(root, "#404040",
                        command=utility.show_settings,
                        text="⚙",
                        font="Arial 20")

settingsFrame = sk.Section(root,  # the container for all settings
                           text="SETTINGS",
                           pack=False,
                           highlightthickness=4,
                           highlightbackground="white")
settingsFrame.label["font"] = "Impact 48"

customisationSettings = sk.Section(settingsFrame,  # section for customisation
                                   text="Customisation")

bgColorSetting = sk.Section(customisationSettings,
                            text="Background color",
                            grid=True)
bgColorPicker = sk.ColorChooser(bgColorSetting, bgColor,
                                lambda color: (utility.change_setting("customisation",
                                                                      "window_background",
                                                                      color)))

bgSlotsSetting = sk.Section(customisationSettings,
                            text="Slots background",
                            grid=True)
bgSlotsPicker = sk.ColorChooser(bgSlotsSetting, bgSlots,
                                lambda color: utility.change_setting("customisation",
                                                                     "slots_background",
                                                                     color))

gameSettings = sk.Section(settingsFrame,
                          text="Game Settings")

slotAmtSetting = sk.Section(gameSettings,
                            text="Slot amount",
                            grid=True)
slotAmtSlider = sk.TextSlider(slotAmtSetting,
                              "234567",
                              slotAmt - 2,
                              lambda value: utility.change_setting("game_settings",
                                                                   "slot_amount",
                                                                   value))

fastSpinSetting = sk.Section(gameSettings,
                             text="Fast spin",
                             grid=True)

check = tk.BooleanVar(value=fastSpin)
fastSpinCheck = tk.Checkbutton(fastSpinSetting,
                               var=check,
                               bg=bgColor,
                               command=lambda: utility.change_setting("game_settings",
                                                                      "fast_spin",
                                                                      str(check.get())),
                               activeforeground="white",
                               activebackground=bgColor)

closeSettingsBtn = sk.Button(settingsFrame, "#404040",
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
