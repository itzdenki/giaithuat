```NOTE: THIS CODE HAS 27 AC and 49 TLE```
def solve(N):
    up = set()
    
    a = 2
    while a * a <= N: 
        b = 2
        p = a * a  
        while p <= N:
            up.add(p)
            b += 1
            p *= a  

        a += 1
    
    return len(up)

N = int(input().strip())
result = solve(N)
print(result + 1)  
```NOTE: THIS CODE HAS 27 AC and 49 TLE```
