from random import randint
from misc import slotAmt, fastSpin, symbols, symData, gui
import threading


def not_valid(msg):
    """
    Tell the user that the Input is not a valid number
    """
    gui.amtInput["bg"] = "#b00000"  # change the text background of the output to a red color
    gui.output["text"] = msg  # change the text of the output-Label


def try_spin(_):
    if gui.spinBtn["state"] == "normal":
        spin()


def spin():
    """
    Run the function to spin with the user's input ->
      -> if it isn't a valid integer number, run not_valid()
      -> if it exceeds the user's balance, run not_valid()
    """
    amt = gui.amtInput.get()
    if not amt:
        return not_valid("Please input a number")
    elif amt == '0':
        return not_valid("Please use at least 1 (one) credit")
    for char in amt:
        if char not in "0123456789":
            return not_valid("Amount is not a number")
    if int(amt) > int(gui.balLabel["text"].split()[1]):  # check if the user's input exceeds the balance
        not_valid("You don't have enough credits")  # change output message; no need for return to stop
    else:
        gui.amtInput["bg"] = "#404040"
        go()  # run the main function to spin


def move_down(ids, n, delay):
    for i in range(n):
        for ID in ids:
            gui.slotCanvas.move(ID, 0, 10)
        gui.slotCanvas.update_idletasks()
        gui.slotCanvas.after(delay)


def spin_anim(ids, n, delay):
    if fastSpin:
        delay, n = 1, 1
    for i in range(n):
        move_down(ids, 6, delay)
        for ID in ids:
            gui.slotCanvas.move(ID, 0, -130)
            rand_sym = symbols[randint(0, len(symbols) - 1)]
            gui.slotCanvas.itemconfig(ID, text=rand_sym, fill=symData[rand_sym]["color"])
        move_down(ids, 7, delay)


def spin_process():
    bal = int(gui.balLabel["text"].split()[1])
    amt = int(gui.amtInput.get())
    bal -= amt  # subtract the amount used from the balance
    gui.balLabel["text"] = f"Balance: {bal}"  # update the balance Label with the new balance
    gui.output["text"] = "spinning..."
    gui.spinBtn["state"] = "disabled"  # lock the spin button
    gui.spinBtn["bg"] = gui.spinBtn.bg
    gui.root.update()

    slot_ids = [gui.sym[key].symbol for key in gui.sym]  # put all slot symbol IDs in a list

    for i in range(slotAmt):
        spin_anim(slot_ids[i:], 5, 10)

    # put each symbol in a list
    slot_values = [gui.slotCanvas.itemcget(ID, "text") for ID in slot_ids]
    # turn the list into a dict {sym: occurrences}
    slot_values = {sym: slot_values.count(sym) for sym in slot_values}

    win = 0
    for key in slot_values:
        if slot_values[key] >= 2:
            win += len(symbols) * slot_values[key] / symData[key]["occurrence"] ** 2
    if round(amt * win):
        bal += round(amt * win)
        gui.output["text"] = f"You spent {amt} credit{'s' if amt - 1 else ''}" \
                             f" and won {round(amt * win)} credit{'s' if round(amt * win) - 1 else ''}!"
    else:
        gui.output["text"] = f"You spent {amt} credit{'s' if amt - 1 else ''} and lost everything."

    gui.balLabel["text"] = f"Balance: {bal}"  # update the balance Label with the new balance
    gui.spinBtn.update()
    gui.spinBtn["state"] = "normal"  # unlock spin button


def go():
    threading.Thread(target=spin_process, daemon=True).start()
