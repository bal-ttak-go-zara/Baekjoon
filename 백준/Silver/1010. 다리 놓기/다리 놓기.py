import math

n = int(input())
for _ in range(n) :
    s,e = map(int,input().split())
    ans = math.factorial(e)/(math.factorial(e-s)*math.factorial(s))
    print(int(ans))