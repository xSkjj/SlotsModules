from modules import gui

# display the elements
gui.header.pack()
gui.settingsBtn.place(x=5, y=5, width=32, height=32)
gui.slotCanvas.pack(padx=4, pady=4)
gui.output.pack(fill='x', padx=8, pady=(24, 4))
gui.userInputs.pack()
gui.balLabel.pack()

# bind functions to events
gui.root.bind("<Return>", gui.func.try_spin)
gui.root.protocol("WM_DELETE_WINDOW", gui.func.on_close)

# keep the window open
gui.root.mainloop()
