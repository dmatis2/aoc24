from collections import defaultdict

rules = []
updates = []

with open('05.in', 'r') as f:
    for line in f:
        if '|' in line:
            rules.append(list(map(int, line.strip().split('|'))))
        if ',' in line:
            updates.append(list(map(int, line.strip().split(','))))

before_nodes = defaultdict(list)
after_nodes = defaultdict(list)

for rule in rules:
    before_nodes[rule[1]].append(rule[0])
    after_nodes[rule[0]].append(rule[1])
     
def ssort(u):
    while True:
        is_done = True
        for i in range(len(u) - 1):
            if [u[i+1], u[i]] in rules:
                u[i], u[i+1] = u[i+1], u[i]
                is_done = False
        if is_done:
            return u
        
def solve(is_part2 = False):
    result = 0
    for update in updates:
        is_valid = True
        for i, c in enumerate(update):
            b, a = update[:i], update[i+1:]
            if any([bb in after_nodes[c] for bb in b]):
                is_valid = False
                continue
            if any([aa in before_nodes[c] for aa in a]):
                is_valid = False
                continue
        if is_valid and not is_part2:
            result += update[len(update)//2]
        if not is_valid and is_part2:
            result += ssort(update)[len(update)//2]
    return result


print(solve())
print(solve(True))