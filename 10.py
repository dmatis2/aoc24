from collections import deque

with open('10.in', 'r') as f:
    grid = [[int(n) for n in list(line.strip())] for line in f]

SIZE = len(grid)
starts = []
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 0:
            starts.append((r, c))

def bfs(start):
    queue = deque([start])

    total = 0

    while queue:
        r, c = queue.popleft()
        height = grid[r][c]

        if height == 9:
            total += 1
            continue

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dy, c + dx
            if 0 <= rr < SIZE and 0 <= cc < SIZE and grid[rr][cc] == height + 1:
                queue.append((rr, cc))

    return total

def dfs(start):
    stack = [start]
    visited = set()
    finished = set()

    while stack:
        r, c = stack.pop()
        if not (0 <= r < SIZE and 0 <= c < SIZE):
            continue
        if (r, c) in visited:
            continue
        if grid[r][c] == 9:
            finished.add((r, c))
            continue
        visited.add((r, c))
        height = grid[r][c]
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr, cc = r + dy, c + dx
            if 0 <= rr < SIZE and 0 <= cc < SIZE and grid[rr][cc] == height + 1 and (rr, cc) not in visited:
                stack.append((rr, cc))
    
    return len(finished)

def solve(is_part2 = False):
    total = 0
    for start in starts:
        total += dfs(start) if not is_part2 else bfs(start)
    return total

print(solve())
print(solve(True))