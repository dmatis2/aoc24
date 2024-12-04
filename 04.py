lines = []
with open('04.in') as f:
    lines = [list(x[:-1]) for x in f.readlines()]

def search_p1(y, x):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    search_count = 0
    for dy, dx in dirs:
        if y + dy < 0 or y + dy >= len(lines):
            continue
        if x + dx < 0 or x + dx >= len(lines[y]):
            continue
        valid = True
        for i in range(1, 4):
            if y + dy * i < 0 or y + dy * i >= len(lines):
                valid = False
                continue
            if x + dx * i < 0 or x + dx * i >= len(lines[y]):
                valid = False
                continue
            if lines[y + dy * i][x + dx * i] != 'XMAS'[i]:
                valid = False
                continue
        if valid:
            search_count += 1
                    
    return search_count

def search_p2(y, x):
    word1 = lines[y - 1][x - 1] + lines[y][x] + lines[y + 1][x + 1]
    word2 = lines[y - 1][x + 1] + lines[y][x] + lines[y + 1][x - 1]

    count = 0
    if word1 in ['MAS', 'SAM'] and word2 in ['MAS', 'SAM']:
        count += 1
    
    return count

def solve_p1():
    count = 0
    for y in range(len(lines)):
        for x in range(len(lines)):
            if lines[y][x] == 'X':
                count += search_p1(y, x)
    return count

def solve_p2():
    count = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines) - 1):
            if lines[y][x] == 'A':
                count += search_p2(y, x)
    return count

print(solve_p1())
print(solve_p2())