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

def place(bStarts,wStarts,change,size=19):
    """This is given starting positions and outputs a board"""
    for x in range(size):
        for y in range(size): 
           # Asigns Color variable
            if f"({x},{y})" in bStarts:
                color = 'b'
            elif f"({x},{y})" in wStarts:
                color = 'w'
            else:
                color = 'x'
            
            # based on 'color' create button
            if color == 'b':
                black_stone = tk.Button(image=black)
                black_stone.grid(column=x,row=y)
            elif color == 'w':
                white_stone = tk.Button(image=white)
                white_stone.grid(column=x,row=y)
            elif color == 'x':
                point = tk.Button(image=empty)
                point.grid(column=x,row=y)

def place_on_list(board):
    """Generates Board from a 2d list"""
    print('Hello World')

def change_board(board,changes):
    """Changes a 2d board list, based on inputs in a list RETURNS A BOARD"""
    print('Board')

x = ['(0,0)']
y = ['(2,2)']

place(x,y,0,)

tk.mainloop()