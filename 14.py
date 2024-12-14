from collections import deque
import re
from time import time
start = time()

with open('14.in') as f:
    lines = [l.strip() for l in f.readlines()]
    robots = []
    for l in lines:
        robots.append([int(x) for x in re.search(r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)', l).groups()])

ROWS = 103
COLS = 101

def after_n_seconds(n):
    r = robots.copy()
    for rr in r:
        rr[0] += (rr[2] * n) % COLS
        rr[1] += (rr[3] * n) % ROWS
        rr[0] %= COLS
        rr[1] %= ROWS
    return r

def get_quadrant(robot):
    MID_X = COLS // 2
    MID_Y = ROWS // 2
    if robot[0] < MID_X and robot[1] < MID_Y:
        return 0
    if robot[0] > MID_X and robot[1] < MID_Y:
        return 1
    if robot[0] < MID_X and robot[1] > MID_Y:
        return 2
    if robot[0] > MID_X and robot[1] > MID_Y:
        return 3
    return -1

after_n_seconds(100)
totals = [0, 0, 0, 0]
for r in robots:
    idx = get_quadrant(r)
    if idx != -1:
        totals[idx] += 1
part1 = totals[0] * totals[1] * totals[2] * totals[3]
print(part1) # PART 1

def count_distance():
    dist = 0
    for i in range(len(robots) - 1 // 10):
        for j in range(i + 1, len(robots) // 10):
            dist += abs(robots[i][0] - robots[j][0]) + abs(robots[i][1] - robots[j][1])
    return dist

min_dist, idx = ROWS * COLS * len(robots), -1
for i in range(10000):
    after_n_seconds(1)
    dist = count_distance()
    if dist < min_dist:
        min_dist = dist
        idx = i

print(idx + 101) # PART 2