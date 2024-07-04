"""Redundant Array
Chef has an array A containing N positive integers.
He can perform the following operation on the array as many times as he likes:

Choose integers L and R such that 1≤L≤R≤N;
Choose a positive integer x; For every index i from L to R (inclusive of both), set A = x
The cost of such an operation is (R−L+1)*x.

Find the minimum cost required to make all the elements of A equal.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists two lines of input.
The first line of each test case contains a single integer N — the size of the array.
The second line contains N space-separated integers A

Output Format
For each test case, output on a new line the minimum cost needed to make all the elements of A equal."""

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        a = int(data[index])
        index += 1
        
        v = list(map(int, data[index:index + a]))
        index += a
        
        from collections import defaultdict
        mp = defaultdict(int)
        
        for num in v:
            mp[num] += 1
        
        ans = float('inf')
        
        for key, value in mp.items():
            r = a - value
            l = key
            l *= r
            ans = min(ans, l)
        
        ans = min(ans, a)
        results.append(ans)
    
    for result in results:
        print(result)

solve()