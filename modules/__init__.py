from configparser import ConfigParser

config = ConfigParser()

config.read(".\\settings.ini") # get window settings from settings.ini


bgColor = config.get ("customisation", "window_background")
bgSlots = config.get ("customisation", "slots_background")

slotAmount = config.getint("game_settings", "slot_amount")

minSlots = 2
maxSlots = 7
slotAmt = minSlots if slotAmount < minSlots else maxSlots if slotAmount > maxSlots else slotAmount
# with Questionmark operator
# slotAmt = (slotAmount < minSlots) ? minslots :
#           (slotAmount > maxSlots) ? maxSlots :
#           slotAmount

# symData = { symbol: { symbol color: color, n/len(symbols): multiplier}}
symData = {
    "🍒": {"color": "#790604", "occurence": 35},
    "🍇": {"color": "#6f2da8", "occurence": 35},
    "🍋": {"color": "#fff44f", "occurence": 35},
    "🍊": {"color": "#ffa500", "occurence": 35},

    "♥": {"color": "brown", "occurence": 10},
    "♦": {"color": "brown", "occurence": 10},
    "♣": {"color": "#101010", "occurence": 10},
    "♠": {"color": "#101010", "occurence": 10},

    "💰": {"color": "#a76222", "occurence": 3},
    "🔔": {"color": "#f6b800", "occurence": 3},
    "🍀": {"color": "#92b832", "occurence": 3},
    "🌞": {"color": "#ffcd35", "occurence": 3},

    "𝟕": {"color": "brown", "occurence": 1}
}

symbols = [key for key in symData for i in range(symData[key]["occurence"])]

bal = 1000


#if __name__ == "__main__":
#    import tkinter as tk
    
#    root = tk.Tk()
#    for i in range(len(symbols)):
#        tk.Label(root, text=symbols[i]).grid(row=0, column=i)
#    root.mainloop()
