class Slot:
    def __init__(self, canv, nth):
        self.canv = canv
        self.symbol = canv.create_text(nth*100+50, 50,
                                    font = ("Consolas", 48))
        self.bg = canv.create_rectangle(nth*100+1, 1,
                                        nth*100+99, 99,
                                        width = 2,
                                        outline = "#692020")

    def set(self, toSet, **kw):
        self.canv.itemconfig(toSet, kw)
    def get(self, toGet, value):
        return self.canv.itemcget(toGet, value)
