grid = [list(row) for row in open('06.in', 'r').read().strip().split('\n')]
ROWS, COLS = len(grid), len(grid[0])
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '^':
            GUARD = (r, c)
            guard = (r, c)
            break

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0

visited = set()
while True:
    visited.add(guard)
    next_row = guard[0] + DIRS[dir][0]
    next_col = guard[1] + DIRS[dir][1]

    if not (0 <= next_row < ROWS and 0 <= next_col < COLS):
        break

    if grid[next_row][next_col] == '#':
        dir = (dir + 1) % 4
    else:
        guard = (next_row, next_col)

print(len(visited))

def generates_loop(r, c):
    if grid[r][c] == '#':
        return False

    visited = set()
    guard = GUARD
    dir = 0
    grid[r][c] = '#'

    while True:
        if (guard[0], guard[1], dir) in visited:
            grid[r][c] = '.'
            return True
        
        visited.add((guard[0], guard[1], dir))
        next_row = guard[0] + DIRS[dir][0]
        next_col = guard[1] + DIRS[dir][1]

        if not (0 <= next_row < ROWS and 0 <= next_col < COLS):
            grid[r][c] = '.'
            return False

        if grid[next_row][next_col] == '#':
            dir = (dir + 1) % 4
        else:
            guard = (next_row, next_col)

total = 0
for r, c in visited:
    total += generates_loop(r, c)
print(total)