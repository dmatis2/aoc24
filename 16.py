from collections import deque
import heapq

with open('16.in') as f:
    grid = [list(line.strip()) for line in f]

for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'S':
            start = (r, c)
        elif cell == 'E':
            end = (r, c)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start, d):
    pq = [(0, start[0], start[1], d, [])]
    visited = set()
    best = float('inf')
    while pq:
        cost, r, c, direction, path = heapq.heappop(pq)
        if (r, c) == end:
            if cost > best:
                print(cost)
                break
            best = cost
            # print(cost)
            continue
        visited.add((r, c, direction))
        if grid[r][c] == '#':
            print(cost)
            break
        for i in range(direction - 1, direction + 2):
            if i != direction:
                rr, cc = r, c
                new_cost = cost + 1000
            else:
                rr, cc = r + DIRS[i % 4][0], c + DIRS[i % 4][1]
                new_cost = cost + 1
            if grid[rr][cc] == '#':
                continue
            if (rr, cc, i % 4) in visited:
                continue
            heapq.heappush(pq, (new_cost, rr, cc, i % 4, path + [(r, c)]))

            

bfs(start, 0)