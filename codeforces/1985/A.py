def thuat_toan(inp):
    lines = inp.splitlines()
    t = int(lines[0])
    result = []
    for i in range(1, t + 1):
        a, b = lines[i].split()
        new_a = b[0] + a[1:]
        new_b = a[0] + b[1:]
        result.append(f"{new_a} {new_b}")
    return "\n".join(result)

def itzdenki2007():
    import sys
    input = sys.stdin.read
    inp = input()
    result = thuat_toan(inp)
    print(result)

if __name__ == "__main__":
    itzdenki2007()