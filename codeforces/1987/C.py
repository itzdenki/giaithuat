import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    n = int(data[index])
    index += 1
    ans = 0
    for i in range(n):
        x = int(data[index + i])
        ans = max(ans, x + i)
    index += n
    print(ans)