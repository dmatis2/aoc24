with open('08.in', 'r') as f:
    grid = [list(l.strip()) for l in f]

antennas = {}
for row, l in enumerate(grid):
    for col, c in enumerate(l):
        if c != '.':
            if c not in antennas:
                antennas[c] = []
            antennas[c].append((row, col))

def has_antenna(row, col):
    return grid[row][col] != '.'

def is_off_grid(row, col):
    return not (0 <= row < len(grid) and 0 <= col < len(grid[0]))

def get_antinode(r1, c1, r2, c2):
    vector = (r2 - r1, c2 - c1)
    return (r1 - vector[0], c1 - vector[1])

def get_antinodes(r1, c1, r2, c2):
    dy, dx = (r2 - r1, c2 - c1)

    values = []
    i = 0
    values.append((r1, c1))
    while not is_off_grid(r1 - dy * i, c1 - dx * i):
        values.append((r1 - dy * i, c1 - dx * i))
        i += 1

    i = 0
    while not is_off_grid(r1 + dy * i, c1 + dx * i):
        values.append((r1 + dy * i, c1 + dx * i))
        i += 1
    return values

def solve(is_part2 = False):
    unique = set()

    for value in antennas.values():
        for i in range(len(value)):
            for j in range(len(value)):
                if i == j:
                    continue
                r1, c1 = value[i]
                r2, c2 = value[j]
                if not is_part2:
                    r3, c3 = get_antinode(r1, c1, r2, c2)
                    if not is_off_grid(r3, c3):
                        unique.add((r3, c3))
                else:
                    nodes = get_antinodes(r1, c1, r2, c2)
                    c = 0
                    for r3, c3 in nodes:
                        c += len(nodes)
                        unique.add((r3, c3))

    return len(unique)

print(solve())
print(solve(True))