"""Perfect Prefixes
A permutation of length N is an array of length N that contains every integer from 1 to N exactly once.
For example, [1,3,2] and [2,1,3] are permutations of length 3, but [2,1,2] and [3,4,2] are not.

The beauty of a permutation P is defined to be the number of prefixes of P that are themselves permutations.
That is, it is the number of integers (1≤i≤N) such that the array [P1, P2, …, Pi] is a permutation of length 𝑖.

You are given a permutation P of length N.
You can perform the following operation on it at most once:

Choose two integers L and R such that 1≤L<R≤N, and L and R have different parities.
That is, if L is odd then R should be even, and vice versa.
Then, for each i=L,L+2,L+4,…,R-1, swap Pi with Pi+1. 
In simpler words, you can choose a subarray of P that has even length, partition it into blocks of length 2, and swap the elements within each block.
For example, if P=[3,1,5,2,6,4] and you choose L=2 and R=5, the resulting permutation is P=[3,5,1,6,2,4].

Find the maximum possible beauty of P after performing at most one such operation.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains a single integer N — the length of the permutation.
The second line contains N space-separated integers P1, P2, …,PN.
Output Format
For each test case, output on a new line the maximum possible beauty of P after performing at most one operation."""

"""Note: this code has TLE in test 4"""

def algo(P, N):
    seen = [0] * (N + 1)
    beauty = 0
    for i in range(N):
        seen[P[i]] = 1
        is_permutation = True
        for j in range(1, i + 2):
            if not seen[j]:
                is_permutation = False
                break
        if is_permutation:
            beauty += 1
    return beauty

T = int(input().strip())
results = []

for _ in range(T):
    N = int(input().strip()) 
    P = list(map(int, input().strip().split()))  
    
    max_beauty = algo(P, N) 

    for L in range(N):
        for R in range(L + 1, N):
            if (L % 2) != (R % 2):
                newP = P[:]
                for i in range(L, R, 2):
                    newP[i], newP[i + 1] = newP[i + 1], newP[i]
                new_beauty = algo(newP, N)
                max_beauty = max(max_beauty, new_beauty)
    
    results.append(max_beauty)

for result in results:
    print(result)