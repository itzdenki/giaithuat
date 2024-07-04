def solve(t, c):
    r = []
    for cs in c:
        n, k = cs
        s = (n * k) - (k - 1)
        r.append(s)
    return r


t = int(input())
c = [tuple(map(int, input().split())) for _ in range(t)]
r = solve(t, c)
for o in r:
    print(o)