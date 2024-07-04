t = int(input().strip())
tc = []

for _ in range(t):
    n, f, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    tc.append((n, f, k, a))

rs = []

for case in tc:
    n, f, k, a = case
    fv = a[f-1]
    
    sv = sorted(a, reverse=True)
    
    tk = sv[:k].count(fv)
    ct = sv.count(fv)
    
    if tk == ct:
        rs.append("YES")
    elif tk == 0:
        rs.append("NO")
    else:
        rs.append("MAYBE")

for r in rs:
    print(r)