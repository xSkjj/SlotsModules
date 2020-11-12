from random import randint
from modules import slotAmt, bal, symbols, symData, gui


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
    try:
        int(amt)
    except ValueError:
        return notValid()
    except:
        gui.amtInput["bg"] = "#b00000"
        gui.output["text"] = "Unexpected error"
    #finally:
        #print(f"amt = {amt}")
    #if amt == "":
        #return notValid()
    #for char in amt:
        #if char not in "0123456789":
            #return notValid()
    if int(amt) > bal:
        gui.amtInput["bg"] = "#b00000"
        gui.output["text"] = "You don't have enough credits"
    else:
        gui.amtInput["bg"] = "#404040"
        go(int(amt))


def go(amt):
    global bal #<- is this bad?
    bal -= amt # subtract the amount used from the balance
    gui.balLabel["text"] = f"Balance: {bal}" # update the balance Label with the new balance
    gui.output["text"] = "spinning..."
    gui.spinBtn["state"] = "disabled" # lock the spin button
    gui.root.update()

    slotIDs = [gui.sym[key].symbol for key in gui.sym] # put all slot symbol IDs in a list
    

    def move_down(i, n, delay):
        if n > 0:
            for id in slotIDs[i:]:
                gui.slotCanvas.move(id, 0, 10)
            gui.slotCanvas.after(delay)
            gui.slotCanvas.update_idletasks()
            move_down(i, n-1, delay)


    def spinAnim(i, n, delay):
        if n > 0:
            move_down(i, 7, delay)
            for id in slotIDs[i:]:
                gui.slotCanvas.move(id, 0, -150)
                randSym = symbols[randint(0, len(symbols)-1)]
                gui.slotCanvas.itemconfig(id, text=randSym, fill=symData[randSym]["color"])
            move_down(i, 8, delay)
            spinAnim(i, n-1, delay)


    for i in range(slotAmt):
        spinAnim(i, 6, 8)


    slotVals = [gui.slotCanvas.itemcget(id, "text") for id in slotIDs] # put the symbol of each slot in a list
    slotVals = {sym : slotVals.count(sym) for sym in slotVals} # turn the list into a dict --> {sym: occurences}

    win = 0
    if len(slotVals) == 1:
        bal += amt * round(len(symData)**(slotAmt - 1)) # amout that gets added if all values are the same
        gui.output["text"] = f"You spent {amt} and won {amt*round(len(symData)**(slotAmt-1))} !!!"
    else:
        for key in slotVals:
            if slotVals[key] >= 2:
                win += 20**2 * slotVals[key] / gui.symData[key]["occurence"]**2
        if win > 0:
            bal += round(amt * win)
            gui.output["text"] = f"You spent {amt} and won {round(amt * win)} !"
        else:
            gui.output["text"] = f"You spent {amt} and lost everything."

    gui.balLabel["text"] = f"Balance: {bal}" # update the balance Label with the new balance
    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal" # unlock spin button
