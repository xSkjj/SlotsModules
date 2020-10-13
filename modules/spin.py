from random import randint

bal = 1000

def trySpin(amt):
    if not isValidNum(amt):
        amtInput["bg"] = "#b00000"
        output["text"] = "Amount is not a valid number"
    elif int(amt) > bal:
        amtInput["bg"] = "#b00000"
        output["text"] = "You don't have enough credits"
    else:
        go(int(amt))


def go(amt):
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "$", "%", "&", "?", "#"]
    output["text"] = "spinning..."

    spinBtn["state"] = "disabled" # lock spin button
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
    spinBtn["state"] = "normal" # unlock spin button
