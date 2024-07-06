from collections import deque

def solve(N, S, T):
    if sorted(S) != sorted(T):
        return -1

    ini = S + '..'
    ts = T + '..'
    q = deque([(ini, 0)]) 
    v = set()
    v.add(ini)
    
    while q:
        cs, op = q.popleft()
        if cs == ts:
            return op
        
        for i in range(N + 1):
            if cs[i] != '.' and cs[i + 1] != '.':
                e = [pos for pos in range(N + 2) if cs[pos] == '.']
                if len(e) != 2:
                    continue  
                
                k1, k2 = e
                if k1 > k2:
                    k1, k2 = k2, k1

                nsl = list(cs)
                nsl[k1] = nsl[i]
                nsl[k2] = nsl[i + 1]
                nsl[i] = nsl[i + 1] = '.'
                ns = ''.join(nsl)
                
                if ns not in v:
                    v.add(ns)
                    q.append((ns, op + 1))
    
    return -1

N = int(input())
S = input().strip()
T = input().strip()


result = solve(N, S, T)
print(result)
