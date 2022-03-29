import tkinter as tk

window = tk.Tk()
window.title("goban")


# create a photoimage variable
black = tk.PhotoImage(file='goBLACK.png')
white = tk.PhotoImage(file='goWHITE.png')
empty = tk.PhotoImage(file='goEMPTY.png')
black = black.zoom(2)

hello = tk.Label(image=black)
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()