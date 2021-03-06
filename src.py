import tkinter, random

size = 4
score = 0
states = []
state_id = None
game_cont = True

def compress(s):
    s = list(filter(lambda x: x != 0, s))
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s[i] *= 2
            global score
            score += s[i]
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
    result = False
    for x in range(size):
        s = []
        for y in range(size):
            p = cells[by_index(x, y)]['text']
            s.append(int(p) if p != '' else 0)
        compressed_s = comp_fun(s)
        if s != compressed_s:
            result = True
        for y in range(size):
            cells[by_index(x, y)]['text'] = compressed_s[y] if compressed_s[y] != 0 else ''
    return result

def save_state():
    state = []
    for x in range(size):
        s = []
        for y in range(size):
            p = cells[by_row(x, y)]['text']
            s.append(int(p) if p != '' else 0)
        state.append(s)
    states.append(state)

def is_game_over():
    for direction in data:
        by_index = direction[0]
        comp_fun = direction[1]
        for x in range(size):
            s = []
            for y in range(size):
                p = cells[by_index(x, y)]['text']
                s.append(int(p) if p != '' else 0)
            compressed_s = comp_fun(s)
            if s != compressed_s:
                return False
    return True

def game_over():
    global game_cont
    game_cont = False
    print("Game over!")
    print("Your maxumim number:", max(map(lambda x: int(x['text']), cells)))
    print("Your score:", score)

def shift(event, d):
    if shift_src(data[d][0], data[d][1]):
        save_state()
        generate()
        return True
    else:
        if is_game_over():
            game_over()

data = [[by_col, compress], [by_row, reverse_compress_reverse], [by_col, reverse_compress_reverse], [by_row, compress]]

def over_r(event):
    while not is_game_over():
        shift(event, random.randint(0, 3))

def over_l_d(event):
    step = 0
    failed = 0
    while True:
        if not shift(event, step % 2 + 1):
            failed += 1
        if failed == 2:
            failed = 0
            if not shift(event, 0):
                failed += 1
            if not shift(event, 2):
                failed += 1
            if failed == 2:
                shift(event, 3)
                shift(event, 1)
                failed = 0
        step += 1
        if is_game_over():
            return

def generate():
    free_cells = list(filter(lambda x: x['text'] == '', cells))
    if len(free_cells) == 0:
        game_over()
    else:
        random.choice(free_cells)['text'] = random.choice(['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '4'])

def roll_back(event):
    if game_cont:
        return
    global state_id
    if state_id == None:
        state_id = len(states) - 1
    state_id -= 1
    for x in range(size):
        for y in range(size):
            cells[by_row(x, y)]['text'] = str(states[state_id][x][y]) if states[state_id][x][y] != 0 else ''

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.focus_set()
frame.pack()
frame.bind('<Up>'   , lambda e: shift(e, 0))
frame.bind('<Right>', lambda e: shift(e, 1))
frame.bind('<Down>' , lambda e: shift(e, 2))
frame.bind('<Left>' , lambda e: shift(e, 3))
frame.bind('<space>', lambda e: over_l_d(e))
frame.bind('<r>'    , lambda e: over_r  (e))
frame.bind('<z>'    , lambda e: roll_back(e))

cells = []
for i in range(size**2):
    btn = tkinter.Button(frame)
    btn.grid(row = i // size, column = i % size)
    cells.append(btn)

generate()
generate()
frame.mainloop()
