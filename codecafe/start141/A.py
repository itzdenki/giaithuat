"""Lucky Clover
Chef heard that four-leaf clovers bring good luck, so he went looking for one.

In his search, Chef found N clovers in total. Out of them, exactly one was a four-leaf clover, and all the others were three-leaf clovers.
How many leaves did Chef collect in total, across all the clovers?

Input Format
The only line of input will contain a single integer N, the number of clovers Chef found.

Output Format
Print one integer: the total number of leaves Chef collected."""

n = int(input())

r = 4+3*(n-1)

print(int(r))