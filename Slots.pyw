from modules import gui, spin

# display the elements
gui.header.pack()
gui.slotsDisplay.pack(pady=4)
gui.output.pack(fill='x', padx=8, pady=(24, 4))
gui.userInputs.pack()
gui.amtInputLabel.grid(column=0, row=0, padx=5)
gui.sub100.grid       (column=1, row=0, padx=1)
gui.sub10.grid        (column=2, row=0, padx=1)
gui.sub1.grid         (column=3, row=0, padx=1)
gui.amtInput.grid     (column=4, row=0, padx=5)
gui.add1.grid         (column=5, row=0, padx=1)
gui.add10.grid        (column=6, row=0, padx=1)
gui.add100.grid       (column=7, row=0, padx=1)
gui.spinBtn.grid      (column=8, row=0, padx=5)
gui.balLabel.pack()


gui.root.mainloop()
