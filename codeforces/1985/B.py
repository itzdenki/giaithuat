def thuat_toan(test_cases):
    results = []
    
    for n in test_cases:
        max_sum = 0
        best_x = 2
        
        for x in range(2, n + 1):
            k = n // x
            current_sum = x * k * (k + 1) // 2
            
            if current_sum > max_sum:
                max_sum = current_sum
                best_x = x
        
        results.append(best_x)
    
    return results

def itzdenki2007():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    t = int(data[0])
    test_cases = [int(data[i]) for i in range(1, t + 1)]
    
    results = thuat_toan(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    itzdenki2007()