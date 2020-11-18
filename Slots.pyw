from modules import gui

# display the elements TODO: YOU HaVE THE WRONG PyCharm
gui.header.pack()
gui.settingsBtn.place(x=5, y=5, width=32, height=32)
gui.slotCanvas.pack(padx=4, pady=4)
gui.output.pack(fill='x', padx=8, pady=(24, 4))
gui.userInputs.pack()
gui.amtInputLabel.grid(column=0, row=0, padx=5)
gui.amtInput.grid(column=1, row=0, padx=5)
gui.spinBtn.grid(column=2, row=0, padx=5)
gui.balLabel.pack()

gui.root.bind("<Return>", gui.func.try_spin)

gui.root.mainloop()
