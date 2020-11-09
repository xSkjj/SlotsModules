from random import randint
from modules import bgSlots, slotFont, symColor, symbols

class Slot:
    def __init__(self, canv, nth):
        self.canv = canv
        self.bgColor = bgSlots
        self.slotFont = slotFont
        self.symColor = symColor
        self.bg = canv.create_rectangle(nth*100+2, 2,
                                        nth*100+98, 98,
                                        width = 0,
                                        fill    = self.bgColor)
        self.sym = canv.create_text(nth*100+50, 50,
                                    text = symbols[randint(0, len(symbols) - 1)],
                                    font = (slotFont, 48, "bold"),
                                    fill = self.symColor,
                                    tags = f"sym{nth}")
