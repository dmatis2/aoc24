from collections import defaultdict

with open('22.in') as f:
    data = list(map(int, f.read().strip().split('\n')))

def next(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


totals = defaultdict(int)

def get_nth(secret, n):
    buyer = [secret % 10]
    for i in range(n):
        secret = next(secret)
        buyer.append(secret % 10)

    visited = set()
    for i in range(len(buyer) - 4):
        a,b,c,d,e = buyer[i:i+5]
        seq = (b-a, c-b, d-c, e-d)
        if seq in visited:
            continue
        visited.add(seq)
        totals[seq] += e

    return secret

print(sum(list(map(lambda x: get_nth(x, 2000), data))))
print(max(totals.values()))