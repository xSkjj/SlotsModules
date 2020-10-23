from random import randint
from modules import slotAmt, bal, symbols, gui


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
    " the "
    global bal # <- bad... maybe
    bal -= amt # subtract the amount used from the balance
    gui.balLabel["text"] = f"Balance: {bal}" # update the balance Label with the new balance
    gui.output["text"] = "spinning..."
    gui.spinBtn["state"] = "disabled" # lock the spin button
    gui.root.update()

    slotIDs = [gui.slotCanvas.find_withtag(f"sym{i}")[0] for i in range(slotAmt)] # put all slot symbol IDs in a list

    for i in range(slotAmt):
        for rand in range(randint(8, 10)):
            for id in slotIDs[i:]:
                sym = symbols[randint(0, len(symbols)-1)]
                gui.slotCanvas.itemconfig(id, text=sym)
            gui.slotCanvas.update_idletasks()
            gui.slotCanvas.after(1)

            
    slotVals = [gui.slotCanvas.itemcget(i, "text") for i in slotIDs] # put the symbol of each slot in a list

    # vvv help me, I'm dying vvv ------------------------------------------------------------------------------------
    # P(X >= 1) = 1 - ((1 - p)**n) --- Probability or something, idk
    # -> p = 1/len(symbols) in my case
    win = 0 # mess
    if slotVals.count(slotVals[0]) == slotAmt:
        bal += round(amt*slotAmt**((len(symbols)-1)/3)) # amout that gets added if all values are the same | mess
        gui.output["text"] = f"You spent {amt} and won {round(amt*slotAmt**((len(symbols)-1)/3))} !!!"
    else:
        for i in slotVals:                #<┐
            if slotVals.count(i) > 1:     #<┼ this is a mess
                win += 1                  #<┘
        if win > 1:
            if win == slotAmt:
                bal += amt * win * (len(symbols)-1) # this is a mess
                gui.output["text"] = f"You spent {amt} and won {amt*slotAmt*(len(symbols)-1)} !!"
            else:
                bal += amt * round((1 / (1 - (1 - 1 / len(symbols)**(win-1))**(slotAmt-1)))/5) # this is a BIG mess
                gui.output["text"] = f"You spent {amt} and won {amt * round((1 / (1 - (1 - 1 / len(symbols)**(win-1))**(slotAmt-1)))/15)} !"
        else:                                                            #<┬ this is the only stuff that's not a mess
            gui.output["text"] = f"You spent {amt} and lost everything." #<┘
    # ^^^ help me, I'm dying ^^^ ------------------------------------------------------------------------------------

    gui.balLabel["text"] = f"Balance: {bal}" # update the balance Label with the new balance
    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal" # unlock spin button