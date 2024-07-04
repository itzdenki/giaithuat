def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        
        b = []
        x = v[0]
        for val in v:
            x = max(x, val)
            if x > val:
                b.append(x - val)
        
        if len(b) == 0:
            print(0)
            continue
        
        b.sort()
        ans = b[-1]
        y = 0
        
        for i in range(len(b)):
            ans += (b[i] - y) * (len(b) - i)
            y = b[i]
        
        print(ans)

if __name__ == "__main__":
    main()