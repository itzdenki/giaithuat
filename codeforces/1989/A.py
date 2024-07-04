def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    tt = int(data[0])
    index = 1
    results = []
    
    for _ in range(tt):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        results.append("YES" if y >= -1 else "NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()