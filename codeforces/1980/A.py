t = int(input())

r = []
for i in range(t):
    n, m = map(int, input().split())
    a = input()
    dif = "ABCDEFG"

    from collections import Counter
    c = Counter(a)

    s = 0
    for difs in dif:
        if c[difs] < m:
            s += (m - c[difs])

    print(s)