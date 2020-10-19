from random import randint
from modules import slotAmt, bal, gui


def notValid():
    """
    Tell the user that the Input is not a valid number
    1. change the text background of the output to a red color
    2. change the text of the output-Label to get the message across
    """
    gui.amtInput["bg"] = "#b00000"
    gui.output["text"] = "Amount is not a valid number"

def trySpin():
    """
    Check if the user's input is a valid integer number
    If it isn't valid, run notValid()
    If it is valid, but greater than the user's balance ->
      -> 1. change the text background of the output to a red color
      -> 2. change the text of the output-Label to get the message across
    If the number doesn't exceed the user's balance, run the function to spin: go()
    """
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
    " the "
    global bal # <- bad
    bal -= amt # subtract the amount used from th balance
    symbols = "0123456789!$%&?#" # all possible symbols that can appear

    gui.output["text"] = "spinning..."
    gui.spinBtn["state"] = "disabled" # lock spin button
    gui.spinBtn.update()
    gui.balLabel["text"] = f"Balance: {bal}" # update the balance label to display the new balance
    gui.balLabel.update()

    slotIDs = [gui.slotsDisplay.find_withtag(f"sym{i}")[0] for i in range(slotAmt)] # this or whatever

    for i in range(slotAmt): # something, probably
        for rand in range(randint(8, 10)):
            sym = symbols[randint(0, len(symbols)-1)]
            for id in slotIDs[i:]: # yeah...
                gui.slotsDisplay.itemconfigure(id, text=sym)
            gui.slotsDisplay.update_idletasks()
            gui.slotsDisplay.after(100)


    slotVals = [gui.slotsDisplay.itemcget(i, "text") for i in slotIDs] # get the ... things
    win = 0
    if slotVals.count(slotVals[0]) == slotAmt: # do things with the things, if the things are all the same
        bal += amt*100
        gui.output["text"] = f"You spent {amt} and won {amt*100} !!!"
    else: # when the
        for i in slotVals:
            if slotVals.count(i) >= slotAmt / 2:
                win += 1
        if win > 0:
            if win == slotAmt:
                bal += amt*50
                gui.output["text"] = f"You spent {amt} and won {amt*50} !!"
            else:
                bal += round(amt * slotAmt / (slotAmt - win))
                gui.output["text"] = f"You spent {amt} and won {round(amt * slotAmt / (slotAmt - win))} !"
        else:
            gui.output["text"] = f"You spent {amt} and lost everything."

    gui.balLabel["text"] = f"Balance: {bal}" # update the balance Label with the new balance - It may or may not have changed. It's more common to be the latter
    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal" # unlock spin button
