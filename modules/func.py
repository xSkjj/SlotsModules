from random import randint
from modules import slotAmt, symbols, symData, gui


def not_valid():
    """
    Tell the user that the Input is not a valid number
    """
    gui.amtInput["bg"] = "#b00000"  # change the text background of the output to a red color
    gui.output["text"] = "Amount is not a valid number"  # change the text of the output-Label


def try_spin():
    """
    Run the function to spin with the user's input ->
      -> if it isn't a valid integer number, run notValid()
      -> if it exceeds the user's balance ->
        -> change the text background of the output to a red color
        -> change the text of the output-Label
    """
    amt = gui.amtInput.get()
    try:
        int(amt)  # check if the user's input can be an int...
    except ValueError:
        return not_valid()  # ... if it isn't, run not_valid() and stop
    # finally:
    #     print(f"amt = {amt}")
    # if amt == "":
    #     return notValid()
    # for char in amt:
    #     if char not in "0123456789":
    #         return notValid()
    if int(amt) > int(gui.balLabel["text"].split()[1]):
        gui.amtInput["bg"] = "#b00000"
        gui.output["text"] = "You don't have enough credits"
    else:
        gui.amtInput["bg"] = "#404040"
        go(int(amt))


def go(amt):  # TODO: add multithreading to improve performance
    bal = int(gui.balLabel["text"].split()[1])
    bal -= amt  # subtract the amount used from the balance
    gui.balLabel["text"] = f"Balance: {bal}"  # update the balance Label with the new balance
    gui.output["text"] = "spinning..."
    gui.spinBtn["state"] = "disabled"  # lock the spin button
    gui.root.update()

    slot_ids = [gui.sym[key].symbol for key in gui.sym]  # put all slot symbol IDs in a list

    def move_down(start_i, n, delay):
        if n > 0:
            for ID in slot_ids[start_i:]:
                gui.slotCanvas.move(ID, 0, 10)
            gui.slotCanvas.after(delay)
            gui.slotCanvas.update_idletasks()
            move_down(start_i, n - 1, delay)

    def spin_anim(start_i, n, delay):
        if n > 0:
            move_down(start_i, 7, delay)
            for ID in slot_ids[start_i:]:
                gui.slotCanvas.move(ID, 0, -150)
                rand_sym = symbols[randint(0, len(symbols) - 1)]
                gui.slotCanvas.itemconfig(ID, text=rand_sym, fill=symData[rand_sym]["color"])
            move_down(start_i, 8, delay)
            spin_anim(start_i, n - 1, delay)

    for i in range(slotAmt):
        spin_anim(i, 6, 8)

    slot_values = [gui.slotCanvas.itemcget(ID, "text") for ID in slot_ids]  # put the symbol of each slot in a list
    slot_values = {sym: slot_values.count(sym) for sym in slot_values}  # turn the list into a dict {sym: occurrences}

    win = 0
    if len(slot_values) == 1:
        bal += amt * round(len(symData) ** (slotAmt - 1))  # amount that gets added if all values are the same
        gui.output["text"] = f"You spent {amt} and won {amt * round(len(symData) ** (slotAmt - 1))} !!!"
    else:
        for key in slot_values:
            if slot_values[key] >= 2:
                win += 6 ** 2 * slot_values[key] / gui.symData[key]["occurrence"] ** 2
        if round(amt * win) > 0:
            bal += round(amt * win)
            gui.output["text"] = f"You spent {amt} and won {round(amt * win)} !"
        else:
            gui.output["text"] = f"You spent {amt} and lost everything."

    gui.balLabel["text"] = f"Balance: {bal}"  # update the balance Label with the new balance
    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal"  # unlock spin button
