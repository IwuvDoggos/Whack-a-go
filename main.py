# Conner Nunley
# Comp Prog 2
# No Cheating

import tkinter as tk

window = tk.Tk()
window.title("goban")

# This will be a tsume go program that gives you predetermined tsume go problems and you must continue in the right order

# create a photoimage variable
black = tk.PhotoImage(file='goBLACK.png')
white = tk.PhotoImage(file='goWHITE.png')
empty = tk.PhotoImage(file='goEMPTY.png')
black = black.zoom(2)
white = white.zoom(2)
empty = empty.zoom(2)

button = tk.Button(image=black)
button.grid(column=0,row=0)

def place(bStarts,wStarts,bMoves,wMoves,size=19):
    """This is given starting positions and outputs a board"""
    for x in range(size):
        for y in range(size):
            if (x,y) in bStarts:
                black_stone = tk.Button(image=black)
                black_stone.grid(column=x,row=y)
            elif (x,y) in wStarts:
                white_stone = tk.Button(image=white)
                white_stone.grid(column=x,row=y)
            else:
                point = tk.Button(image=empty)
                point.grid(column=x,row=y)


tk.mainloop()