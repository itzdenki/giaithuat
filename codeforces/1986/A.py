import math

t = int(input())

for i in range(t):
  x = list(map(int, input().split()))
  x.sort()
  print(abs(x[2] - x[1]) + abs(x[1] - x[1]) + abs(x[1] - x[0]))
  