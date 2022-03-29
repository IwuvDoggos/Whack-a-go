import tkinter as tk

window = tk.Tk()
window.title("goban")


# create a photoimage variable
black = tk.PhotoImage(file='goBLACK.png')
white = tk.PhotoImage(file='goWHITE.png')
empty = tk.PhotoImage(file='goEMPTY.png')
black = black.zoom(2)
white = white.zoom(2)
empty = empty.zoom(2)

button = tk.Button(image=black)
button.grid(column=0,row=0)

tk.mainloop()