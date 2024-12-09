with open('09.in', 'r') as f:
    input = [int(n) for n in list(f.read().strip())]

MAX_IDX = 0

def expand(data):
    global MAX_IDX
    expanded = []
    for i, n in enumerate(data):
        expanded += [str(i // 2)] * n if i % 2 == 0 else ['.'] * n
        MAX_IDX = i // 2

    return expanded

def move(data):
    l, r = 0, len(data) - 1
    while data[l] != '.':
        l += 1
    while data[r] == '.':
        r -= 1

    while l < r:
        data[l], data[r] = data[r], data[l]
        while data[l] != '.':
            l += 1
        while data[r] == '.':
            r -= 1
    return data

total = 0
for i, v in enumerate(move(expand(input))):
    if v != '.':
        total += (int(v) * i)

print(total)

id = 0
files = {}
blanks = []
position = 0

for i, v in enumerate(input):
    if i % 2 == 0:
        if v == 0:
            raise ValueError('Zero length file')
        files[id] = (position, v)
        id += 1
    else:
        if v > 0:
            blanks.append((position, v))
    position += v

while id > 0:
    id -= 1
    position, length = files[id]
    for i, blank in enumerate(blanks):
        if blank[0] >= position:
            blanks = blanks[:i]
            break
        if blank[1] == length:
            files[id] = (blank[0], length)
            blanks.pop(i)
            break
        elif blank[1] > length:
            files[id] = (blank[0], length)
            blanks[i] = (blank[0] + length, blank[1] - length)
            break

total = 0
for id, (position, length) in files.items():
    for i in range(position, position + length):
        total += id * i

print(total)