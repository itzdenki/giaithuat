def solve(n, k, a):
    a.sort()

    md = float('inf')

    for i in range(k + 1):
        maxw = a[i + (n - k) - 1]
        minw = a[i]
        d = maxw - minw
        md = min(md, d)

    return md

n, k = map(int, input().split())
a = list(map(int, input().split()))

r = solve(n, k, a)
print(r)