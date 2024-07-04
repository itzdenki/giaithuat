def solve(t, test_cases):
    results = []
    for i in range(t):
        x1, y1 = test_cases[i][0]
        x2, y2 = test_cases[i][1]
        
        if (x1 > y1 and x2 > y2) or (x1 < y1 and x2 < y2):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    test_cases.append([(x1, y1), (x2, y2)])

results = solve(t, test_cases)
for result in results:
    print(result)