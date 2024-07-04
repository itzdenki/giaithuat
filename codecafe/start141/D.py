"""
Amphibian Escape
Chef is building a robot frog, which he would like to be able to climb out of a well quickly.

The well has a height of H units. Initially, the frog is placed at the bottom of the well.

Let A denote the jumping power of the frog, and B denote the slipperiness of the well's wall.
The frog is initially at position X=0.
Every second, the following two steps happen in order:

First, the frog will jump A units upwards along the wall. That is, X will increase by A.
If it reaches a height of H units or greater (i.e if X≥H) with this jump, it's considered to have climbed out of the well, and the process stops.
Next, if it's still within the well, it will then slip B units downwards — that is, X will reduce by B.
Note that X cannot fall below 0, more formally, X gets set to max(0,X - B).
Chef hasn't decided on the jumping power of the robot frog, and also doesn't know the slipperiness of the well.

You are given integers N,K, and H.
Count the number of pairs (A,B) such that: 1≤A≤N and 1≤B≤N.
If the frog had jumping power A and the well's slipperiness is B, the frog can escape the well (which has height H) within K seconds.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The first and only line of each test case contains 3 space-separated integers N,K, and H — the bounds on A and B, the time by which the frog must escape the well, and the height of the well.
Output Format
For each test case, output on a new line the number of pairs (A,B) that allow the frog to escape."""

def solve():
    T = int(input())
    for _ in range(T):
        N, K, H = map(int, input().split())
        v = 0
        for A in range(1, N + 1):
            for B in range(1, N + 1):
                if A >= H:
                    v += 1
                elif A > B:
                    s = A - B
                    m = K * s + B
                    if m >= H:
                        v += 1
        print(v)

solve()