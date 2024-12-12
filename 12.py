from collections import deque, defaultdict

with open('12.in', 'r') as f:
    grid = [list(line.strip()) for line in f]

ROWS = len(grid)
COLS = len(grid[0])

visited = set()

p1 = 0
p2 = 0

for r in range(ROWS):
    for c in range(COLS):
        if (r, c) in visited:
            continue
        queue = deque([(r, c)])

        facing = defaultdict(set)
        count = 0
        perimeter = 0
        while queue:
            rr, cc = queue.popleft()
            if (rr, cc) in visited:
                continue
            visited.add((rr, cc))
            count += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rrr = rr + dr
                ccc = cc + dc
                if 0 <= rrr < ROWS and 0 <= ccc < COLS and grid[rrr][ccc] == grid[rr][cc]:
                    queue.append((rrr, ccc))
                else:
                    perimeter += 1
                    facing[(dr, dc)].add((rr, cc))
        p1 += count * perimeter

        sides = 0
        for (dr2, dc2), values in facing.items():
            facing_visited = set()
            for r2, c2 in values:
                if (r2, c2) in facing_visited:
                    continue
                
                sides += 1
                q = deque([(r2, c2)])

                while q:
                    rr2, cc2 = q.popleft()
                    if (rr2, cc2) in facing_visited:
                        continue
                    facing_visited.add((rr2, cc2))
                    for ddr2, ddc2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        rrr2 = rr2 + ddr2
                        ccc2 = cc2 + ddc2
                        if (rrr2, ccc2) in values:
                            q.append((rrr2, ccc2))

        p2 += count * sides

print(p1)
print(p2)