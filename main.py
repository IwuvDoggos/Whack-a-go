import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

# create a photoimage variable
img = tk.PhotoImage(file='vector.png')


hello = tk.Label(image=img)
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()