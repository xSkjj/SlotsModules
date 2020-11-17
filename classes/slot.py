class Slot:
    def __init__(self, canvas, nth):
        self.canvas = canvas
        self.symbol = canvas.create_text(nth * 100 + 50, 50,
                                         font=("Consolas", 48))
        self.bg = canvas.create_rectangle(nth * 100 + 1, 1,
                                          nth * 100 + 99, 99,
                                          width=2,
                                          outline="#692020")

    def set(self, to_set, **kw):
        self.canvas.itemconfig(to_set, kw)

    def get(self, to_get, value):
        return self.canvas.itemcget(to_get, value)
