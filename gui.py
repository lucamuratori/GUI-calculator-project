import tkinter
from tkinter import ttk

# TODO: create the calculator gui
root = tkinter.Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

# buttons
ttk.Button(frame, text="0").grid(column=1, row=6)
ttk.Button(frame, text=".").grid(column=2, row=6)
ttk.Button(frame, text="=").grid(column=4, row=6)

# row number 5
ttk.Button(frame, text="1").grid(column=0, row=5)
ttk.Button(frame, text="2").grid(column=1, row=5)
ttk.Button(frame, text="3").grid(column=2, row=5)
ttk.Button(frame, text="^").grid(column=3, row=5)
ttk.Button(frame, text="+").grid(column=4, row=5)

# row number 4
ttk.Button(frame, text="4").grid(column=0, row=4)
ttk.Button(frame, text="5").grid(column=1, row=4)
ttk.Button(frame, text="6").grid(column=2, row=4)
ttk.Button(frame, text="n!").grid(column=3, row=4)
ttk.Button(frame, text="-").grid(column=4, row=4)

# row number 3
ttk.Button(frame, text="7").grid(column=0, row=3)
ttk.Button(frame, text="8").grid(column=1, row=3)
ttk.Button(frame, text="9").grid(column=2, row=3)
ttk.Button(frame, text="√").grid(column=3, row=3)
ttk.Button(frame, text="x").grid(column=4, row=3)

# row number 2
ttk.Button(frame, text="AC").grid(column=0, row=2)
ttk.Button(frame, text="⌫").grid(column=1, row=2)
ttk.Button(frame, text="%").grid(column=2, row=2)
ttk.Button(frame, text="root").grid(column=3, row=2)
ttk.Button(frame, text="÷").grid(column=4, row=2)

root.mainloop()
# TODO: link all operations to the buttons on the calculator


