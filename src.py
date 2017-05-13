import tkinter, random

size = 4

def shift(event, d):
    if d == 1:
        for row in range(size):
            s = []
            for col in range(size):
                p = cells[col + size * row]['text']
                if p != '':
                    s.append(int(p))
            s = s[::-1]
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    s[i] *= 2
                    del s[i+1]
                i += 1
            s = s[::-1]
            for col in range(size):
                if col < (size - len(s)):
                    cells[col + size * row]['text'] = ''
                else:
                    cells[col + size * row]['text'] = s[col - (size - len(s))]
    if d == 3:
        for row in range(size):
            s = []
            for col in range(size):
                p = cells[col + size * row]['text']
                if p != '':
                    s.append(int(p))
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    s[i] *= 2
                    del s[i+1]
                i += 1
            for col in range(size):
                if col < len(s):
                    cells[col + size * row]['text'] = s[col]
                else:
                    cells[col + size * row]['text'] = ''
    if d == 0:
        for col in range(size):
            s = []
            for row in range(size):
                p = cells[col + size * row]['text']
                if p != '':
                    s.append(int(p))
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    s[i] *= 2
                    del s[i+1]
                i += 1
            for row in range(size):
                if row < len(s):
                    cells[col + size * row]['text'] = s[row]
                else:
                    cells[col + size * row]['text'] = ''
    if d == 2:
        for col in range(size):
            s = []
            for row in range(size):
                p = cells[col + size * row]['text']
                if p != '':
                    s.append(int(p))
            s = s[::-1]
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    s[i] *= 2
                    del s[i+1]
                i += 1
            s = s[::-1]
            for row in range(size):
                if row < (size - len(s)):
                    cells[col + size * row]['text'] = ''
                else:
                    cells[col + size * row]['text'] = s[row - (size - len(s))]
    generate()

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

cells = []
for i in range(size**2):
    btn = tkinter.Button(frame)
    btn.grid(row = i // size, column = i % size)
    cells.append(btn)

generate()
generate()
frame.mainloop()
