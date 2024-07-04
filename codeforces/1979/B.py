def algo(n):
    if n == 0:
        return 32 
    count = 0
    while (n & 1) == 0:
        n >>= 1
        count += 1
    return count

def algo1(x, y):
    return 1 << algo(x ^ y)

t = int(input().strip())

results = []
for _ in range(t):
    x, y = map(int, input().strip().split())
    result = algo1(x, y)
    results.append(result)

for result in results:
    print(result)