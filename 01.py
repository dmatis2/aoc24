from collections import defaultdict

d = defaultdict(int)

with open('01.in', 'r') as f:
    l = []
    r = []
    for line in f:
        ll, rr = list(map(int, line.split()))
        l.append(ll)
        r.append(rr)
        d[rr] += 1
    l.sort()
    r.sort()
    x = [abs(l[i]-r[i]) for i in range(len(l))]
    print(sum(x))
    total = sum([n * d[n] for n in l])
    print(total)