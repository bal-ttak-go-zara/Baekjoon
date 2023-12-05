"""
1 1 1 2 2 3 4 5 7 9 12 16 21 28...
P(6) = P(4) + P(3)
P(7) = P(5) + P(4)
P(10) = P(8) + P(7)
P(n) = P(n-2) + P(n-3)
"""

import sys

memo = {}

def P(n) :
    result = 0
    
    if n in memo :
        return memo[n]
    
    if n in [1,2,3] :
        result = 1

    elif n in [4,5] :
        result = 2

    else :
        result = P(n-2) + P(n-3)

    memo[n] = result
    return result
 
for _ in range(int(input())) :
    n = int(sys.stdin.readline())
    print(P(n))
