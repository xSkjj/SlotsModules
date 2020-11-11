from random import randint
from modules import symData, symbols

class Slot:
    def __init__(self, canv, nth):
        randSym = symbols[randint(0, len(symbols) - 1)]
        self.canv = canv
        self.sym = canv.create_text(nth*100+50, 50,
                                    text = randSym,
                                    font = ("Consolas", 48),
                                    fill = symData[randSym]["color"],
                                    tags = f"sym{nth}")
        self.bg = canv.create_rectangle(nth*100+1, 1,
                                        nth*100+99, 99,
                                        width = 2,
                                        outline = "#692020")
