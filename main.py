# Conner Nunley
# Comp Prog 2
# No Cheating

from re import X
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

def place(bStarts,wStarts,bMoves,wMoves,size=19):
    """This is given starting positions and outputs a board"""
    for x in range(size):
        for y in range(size):
            if f"({x},{y})" in bStarts:
                black_stone = tk.Button(image=black)
                black_stone.grid(column=x,row=y)
            elif f"({x},{y})" in wStarts:
                white_stone = tk.Button(image=white)
                white_stone.grid(column=x,row=y)
            else:
                point = tk.Button(image=empty)
                point.grid(column=x,row=y)


x = ['(0,0)']
y = ['(2,2)']

place(x,y,0,0)

tk.mainloop()