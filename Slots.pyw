from modules import gui

# display the elements
gui.header.pack()
gui.slotsDisplay.pack(pady=4)
gui.output.pack(fill='x', padx=8, pady=(24, 4))
gui.userInputs.pack()
gui.amtInputLabel.grid(column=0, row=0, padx=5)
gui.amtInput.grid     (column=1, row=0, padx=5)
gui.spinBtn.grid      (column=2, row=0, padx=5)
gui.balLabel.pack()


gui.root.mainloop()
