class Slot:
    def __init__(self, canvas, nth):
        self.canvas = canvas
        self.symbol = self.canvas.create_text(nth * 100 + 50, 50,
                                              font=("Consolas", 48))
        self.bg = self.canvas.create_rectangle(nth * 100 + 1, 1,
                                               nth * 100 + 99, 99,
                                               width=2,
                                               outline="#692020")

    def set(self, to_set, **kwargs):
        self.canvas.itemconfig(to_set, kwargs)

    def get(self, to_get, value):
        return self.canvas.itemcget(to_get, value)
