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

def reverse_compress_reverse(s):
    return compress(s[::-1])[::-1]

def by_row(x, y):
    return y + size * x

def by_col(x, y):
    return x + size * y

def shift_src(by_index, comp_fun):
    for x in range(size):
        s = []
        for y in range(size):
            p = cells[by_index(x, y)]['text']
            s.append(int(p) if p != '' else 0)
        s = comp_fun(s)
        for y in range(size):
            cells[by_index(x, y)]['text'] = s[y] if s[y] != 0 else ''

def shift(event, d):
    shift_src(data[d][0], data[d][1])
    generate()

data = [[by_col, compress], [by_row, reverse_compress_reverse], [by_col, reverse_compress_reverse], [by_row, compress]]

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
