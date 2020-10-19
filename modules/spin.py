from random import randint
from modules import gui


def notValid():
    gui.amtInput["bg"] = "#b00000"
    gui.output["text"] = "Amount is not a valid number"

def trySpin():
    amt = gui.amtInput.get()
    if amt == "":
        return notValid()
    for char in amt:
        if char not in "0123456789":
            return notValid()
    if int(amt) > bal:
        gui.amtInput["bg"] = "#b00000"
        gui.output["text"] = "You don't have enough credits"
    else:
        gui.amtInput["bg"] = "#404040"
        go(int(amt))


def go(amt):
    symbols = "0123456789!$%&?#"
    gui.output["text"] = "spinning..."

    gui.spinBtn["state"] = "disabled" # lock spin button
    gui.spinBtn.update()

    global bal
    bal -= amt

    gui.balLabel["text"] = f"Balance: {bal}"
    gui.balLabel.update()

    IDsymA = gui.slotsDisplay.find_withtag("symA")[0]
    IDsymB = gui.slotsDisplay.find_withtag("symB")[0]
    IDsymC = gui.slotsDisplay.find_withtag("symC")[0]

    for i in range(0, randint(8, 10)): # range(0, 4) is (0, 1, 2, 3)...
        symA = symB = symC = symbols[randint(0, len(symbols)-1)]
        gui.slotsDisplay.itemconfigure(IDsymA, text=symA)
        gui.slotsDisplay.itemconfigure(IDsymB, text=symB)
        gui.slotsDisplay.itemconfigure(IDsymC, text=symC)
        gui.slotsDisplay.update_idletasks()
        gui.slotsDisplay.after(100)
    for i in range(0, randint(11, 13)): # ...but randint(0, 4) is (0, 1, 2, 3, 4)...
        symB = symC = symbols[randint(0, len(symbols)-1)]
        gui.slotsDisplay.itemconfigure(IDsymB, text=symB)
        gui.slotsDisplay.itemconfigure(IDsymC, text=symC)
        gui.slotsDisplay.update_idletasks()
        gui.slotsDisplay.after(100)
    for i in range(0, randint(14, 16)): # ...this is bullshit
        symC = symbols[randint(0, len(symbols)-1)]
        gui.slotsDisplay.itemconfigure(IDsymC, text=symC)
        gui.slotsDisplay.update_idletasks()
        gui.slotsDisplay.after(100)

    if symA == symB and symB == symC:
        bal += amt*100
        gui.output["text"] = f"You spent {amt} and won {amt*100} !!!"
    elif symA == symB or symA == symC or symB == symC:
        bal += amt*3
        gui.output["text"] = f"You spent {amt} and won {amt*3} !"
    else:
        gui.output["text"] = f"You spent {amt} and lost everything."

    gui.balLabel["text"] = f"Balance: {bal}"

    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal" # unlock spin button
