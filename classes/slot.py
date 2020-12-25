class Slot:
    def __init__(self, canvas, nth):
        self.canvas = canvas
        self.symbol = self.canvas.create_text(nth * 120 + 60, 60,
                                              font="Consolas 42")
        self.bg = self.canvas.create_rectangle(nth * 120 + 12, 12,
                                               nth * 120 + 108, 108,
                                               width=24,
                                               outline="#692020")

    def set(self, to_set, **kwargs):
        self.canvas.itemconfig(to_set, kwargs)

    def get(self, to_get, value):
        return self.canvas.itemcget(to_get, value)
