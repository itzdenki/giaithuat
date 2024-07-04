"""Nearly Equal
The Hamming distance between two pairs of strings of equal length is defined to be the number of positions at which they contain different characters.
For example, the Hamming distance between strings "there" and "shire" is 
2 (their first and third characters are different), while the Hamming distance between 
"order" and "chaos" is 5, since they differ at every position.

Chef has a string A of length N. Chef's favorite string is B, which has length M. It is known that M≤N.

Find the minimum Hamming distance between B and some contiguous substring of A that has length M.A substring of a string is obtained by deleting some (possibly, zero) characters from its beginning and some (possibly, zero) characters from its end.
For example, "abc", "bc", and "cd" are substrings of "abcd", but "ac" is not.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three lines of input.
The first line of each test case contains two space-separated integers N and M — the lengths of strings A and B, respectively.
The second line contains the string A, consisting of N lowercase English letters.
The third line contains the string B, consisting of M lowercase English letters.
Output Format
For each test case, output on a new line the minimum possible Hamming distance between B and some length M substring of A"""

def solve(T, test_cases):
    results = []
    for i in range(T):
        N, M = test_cases[i][0]
        A = test_cases[i][1]
        B = test_cases[i][2]
        
        min_distance = M  
        
        for j in range(N - M + 1):
            substring = A[j:j+M]
            distance = sum(1 for x, y in zip(substring, B) if x != y)
            if distance < min_distance:
                min_distance = distance
                
        results.append(min_distance)
    
    return results

import sys
input = sys.stdin.read

data = input().split()
T = int(data[0])
index = 1
test_cases = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1])
    A = data[index + 2]
    B = data[index + 3]
    test_cases.append(((N, M), A, B))
    index += 4

results = solve(T, test_cases)
for result in results:
    print(result)