import tkinter, random

size = 4

def compress(s):
    s = list(filter(lambda x: x != 0, s))
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s[i] *= 2
            del s[i+1]
        i += 1
    while len(s) < size:
        s.append(0)
    return s

def shift(event, d):
    if d == 1:
        for row in range(size):
            s = []
            for col in range(size):
                p = cells[col + size * row]['text']
                s.append(int(p) if p != '' else 0)
            s = compress(s[::-1])[::-1]
            for col in range(size):
                cells[col + size * row]['text'] = s[col] if s[col] != 0 else ''
    if d == 3:
        for row in range(size):
            s = []
            for col in range(size):
                p = cells[col + size * row]['text']
                s.append(int(p) if p != '' else 0)
            s = compress(s)
            for col in range(size):
                cells[col + size * row]['text'] = s[col] if s[col] != 0 else ''
    if d == 0:
        for col in range(size):
            s = []
            for row in range(size):
                p = cells[col + size * row]['text']
                s.append(int(p) if p != '' else 0)
            s = compress(s)
            for row in range(size):
                cells[col + size * row]['text'] = s[row] if s[row] != 0 else ''
    if d == 2:
        for col in range(size):
            s = []
            for row in range(size):
                p = cells[col + size * row]['text']
                s.append(int(p) if p != '' else 0)
            s = compress(s[::-1])[::-1]
            for row in range(size):
                cells[col + size * row]['text'] = s[row] if s[row] != 0 else ''
    generate()

def over(event):
    step = 0
    while step < 1000:
        print(step)
        shift(event, step % 4)
        step += 1

def generate():
    free_cells = []
    for i in range(len(cells)):
        if cells[i]['text'] == '':
            free_cells.append(i)
    if len(free_cells) == 0:
        print("Game over")
    else:
        k = random.choice(free_cells)
        cells[k]['text'] = '2'

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.focus_set()
frame.pack()
frame.bind('<Up>'   , lambda e: shift(e, 0))
frame.bind('<Right>', lambda e: shift(e, 1))
frame.bind('<Down>' , lambda e: shift(e, 2))
frame.bind('<Left>' , lambda e: shift(e, 3))
frame.bind('<R>' , lambda e: over(e))

cells = []
for i in range(size**2):
    btn = tkinter.Button(frame)
    btn.grid(row = i // size, column = i % size)
    cells.append(btn)

generate()
generate()
frame.mainloop()
