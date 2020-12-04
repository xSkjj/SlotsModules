class Slot:
    def __init__(self, canvas, nth):
        self.canvas = canvas
        self.symbol = self.canvas.create_text(nth * 120 + 60, 60,
                                              font=("Consolas", 56))
        self.bg = self.canvas.create_rectangle(nth * 120 + 2, 2,
                                               nth * 120 + 118, 118,
                                               width=4,
                                               outline="#692020")

    def set(self, to_set, **kwargs):
        self.canvas.itemconfig(to_set, kwargs)

    def get(self, to_get, value):
        return self.canvas.itemcget(to_get, value)
