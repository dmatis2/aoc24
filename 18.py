from collections import deque
from time import time
start = time()

with open('18.in') as f:
    data = [tuple(map(int, l.split(',')[::-1])) for l in f.read().strip().split('\n')]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(blocks):
    q = deque([(0, 0, 0, [])])
    visited = set()
    while q:
        y, x, steps, path = q.popleft()
        if (y, x) == (70, 70):
            return path
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if (y, x) in blocks:
            continue
        for dy, dx in DIRS:
            yy, xx = y + dy, x + dx
            if 0 <= yy < 71 and 0 <= xx < 71:
                q.append((yy, xx, steps + 1, path + [(y, x)]))
    return None

def binary_search():
    lo, hi = 0, len(data) + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if bfs(data[:mid+1]) == None:
            hi = mid
        else:
            lo = mid + 1
    return ','.join(list(map(str,data[lo][::-1])))

print(len(bfs(data[:1024])))
print(binary_search())