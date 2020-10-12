import tkinter as tk

# window settings
icon = r".\assets\icon.ico" # icon in the top left corner
title = "Slots"             # Title at the top of the window
minWidth = 400              # minimum width you can resize the window to
minHeight = 255             # minimum height you can resize the window to
maxWidth = 400              # maximum width you can resize the window to
maxHeight = 255             # maximum height you can resize the window to
windowWidth = "400"         # the width of the window when starting
windowHeight = "255"        # the height of the window when starting
offsetx = "200"             # distance between the window's and screen's left edge
offsety = "200"             # distance between the window's and screen's top edge
bgColor = "#202020"         # background color of the window

# apply window settings
root = tk.Tk()
root.iconbitmap(icon)
root.title(title)
root.minsize(minWidth, minHeight)
root.maxsize(maxWidth, maxHeight)
root.geometry((windowWidth + "x" + windowHeight + "+" + offsetx + "+" + offsety))
root["background"] = bgColor



# try to fire the slots function with the given input
def trySpin():
    amt = amtInput.get()
    try:
        int(amt)
        amtInput["bg"] = "#404040"
        slots(int(amt))
    except: # if it fails, tell the user why
        amtInput["bg"] = "#b00000"
        if amt == "":
            output["text"] = "Amount is empty"
        else:
            output["text"] = "Amount is not a valid number"

# slots function
bal = 1000
def slots(amt):
    global bal

    # if the amount is higher than the balance, stop the function
    if amt > bal:
        amtInput["bg"] = "#b00000"
        output["text"] = "You don't have enough credits."
        return

    # slots stuff or something
    output["text"] = "spinning..."

    from random import randint

    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]

    spinBtn["state"] = "disabled"
    spinBtn.update()

    bal -= amt

    balLabel["text"] = f"Balance: {bal}"
    balLabel.update()

    IDsymA = slotsDisplay.find_withtag("symA")[0]
    IDsymB = slotsDisplay.find_withtag("symB")[0]
    IDsymC = slotsDisplay.find_withtag("symC")[0]

    for i in range(0, randint(8, 10)): # range(0, 4) is (0, 1, 2, 3)...
        symA = symB = symC = symbols[randint(0, len(symbols)-1)]
        slotsDisplay.itemconfigure(IDsymA, text=symA)
        slotsDisplay.itemconfigure(IDsymB, text=symB)
        slotsDisplay.itemconfigure(IDsymC, text=symC)
        slotsDisplay.update_idletasks()
        slotsDisplay.after(100)
    for i in range(0, randint(11, 13)): # ...but randint(0, 4) is (0, 1, 2, 3, 4)...
        symB = symC = symbols[randint(0, len(symbols)-1)]
        slotsDisplay.itemconfigure(IDsymB, text=symB)
        slotsDisplay.itemconfigure(IDsymC, text=symC)
        slotsDisplay.update_idletasks()
        slotsDisplay.after(100)
    for i in range(0, randint(14, 16)): # ...this is bullshit
        symC = symbols[randint(0, len(symbols)-1)]
        slotsDisplay.itemconfigure(IDsymC, text=symC)
        slotsDisplay.update_idletasks()
        slotsDisplay.after(100)

    if symA == symB and symB == symC:
        bal += amt*100
        output["text"] = f"You spent {amt} and won {amt*100} !!!"
    elif symA == symB or symA == symC or symB == symC:
        bal += amt*3
        output["text"] = f"You spent {amt} and won {amt*3} !"
    else:
        output["text"] = f"You spent {amt} and lost everything."

    balLabel["text"] = f"Balance: {bal}"

    spinBtn.update()
    spinBtn["state"] = "normal"


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
                 command = trySpin,
                 text    = "spin",
                 font    = "Arial 10 bold",
                 fg      = "#050",
                 bg      = "light green",
                 relief  = "flat")

balLabel = tk.Label(root,
                 text = f"Balance: {bal}",
                 font = "Arial 10 bold",
                 fg   = "gold",
                 bg   = bgColor)

# display the elements
header.pack()
slotsDisplay.pack(pady=4)
output.pack(fill='x', padx=8, pady=(24, 4))
userInputs.pack()
amtInputLabel.grid(column=0, row=0, padx=5)
amtInput.grid     (column=1, row=0, padx=5)
spinBtn.grid      (column=2, row=0, padx=5)
amtInput.insert(0, "0")
balLabel.pack()


root.mainloop()
