from random import randint
from modules import slotAmt, bal, gui


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
    global bal
    bal -= amt
    symbols = "0123456789!$%&?#"

    gui.output["text"] = "spinning..."
    gui.spinBtn["state"] = "disabled" # lock spin button
    gui.spinBtn.update()
    gui.balLabel["text"] = f"Balance: {bal}"
    gui.balLabel.update()

    slotIDs = [gui.slotsDisplay.find_withtag(f"sym{i}")[0] for i in range(slotAmt)]

    for i in range(slotAmt):
        for rand in range(randint(8, 10)):
            sym = symbols[randint(0, len(symbols)-1)]
            for id in slotIDs[i:]:
                gui.slotsDisplay.itemconfigure(id, text=sym)
            gui.slotsDisplay.update_idletasks()
            gui.slotsDisplay.after(100)


    slotVals = [gui.slotsDisplay.itemcget(i, "text") for i in slotIDs]
    win = 0
    if slotVals.count(slotVals[0]) == slotAmt:
        bal += amt*100
        gui.output["text"] = f"You spent {amt} and won {amt*100} !!!"
    else:
        for i in slotVals:
            if slotVals.count(i) >= slotAmt / 2:
                win += 1
        if win > 0:
            if not win == slotAmt:
                bal += round(amt * slotAmt / (slotAmt - win))
                gui.output["text"] = f"You spent {amt} and won {round(amt * slotAmt / (slotAmt - win))} !"
            else:
                bal += amt*50
                gui.output["text"] = f"You spent {amt} and won {amt*50} !!"
        else:
            gui.output["text"] = f"You spent {amt} and lost everything."

    gui.balLabel["text"] = f"Balance: {bal}"
    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal" # unlock spin button
