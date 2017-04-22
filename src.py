import tkinter, random

size = 4

def shift(event, d):
    pass

def generate():
    for i in range(2):
        k = random.randint(0, size**2 - 1)
        while k in numbers:
            k = random.randint(0, size**2 - 1)
        numbers.append(k)
        cells[k]['text'] = '2'

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.focus_set()
frame.pack()
frame.bind('<Up>'   , lambda e: shift(e, 0))
frame.bind('<Right>', lambda e: shift(e, 1))
frame.bind('<Down>' , lambda e: shift(e, 2))
frame.bind('<Left>' , lambda e: shift(e, 3))

numbers = []
cells = []
for i in range(size**2):
    btn = tkinter.Button(frame)
    btn.grid(row = i // size, column = i % size)
    cells.append(btn)

generate()
frame.mainloop()
