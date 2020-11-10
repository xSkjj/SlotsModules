from random import randint
from modules import symColor, symbols

class Slot:
    def __init__(self, canv, nth):
        self.canv = canv
        self.symColor = symColor
        self.sym = canv.create_text(nth*100+50, 50,
                                    text = symbols[randint(0, len(symbols) - 1)],
                                    font = ("Consolas", 48),
                                    fill = self.symColor,
                                    tags = f"sym{nth}")
        self.bg = canv.create_rectangle(nth*100+1, 1,
                                        nth*100+99, 99,
                                        width = 2,
                                        outline = "#692020")
