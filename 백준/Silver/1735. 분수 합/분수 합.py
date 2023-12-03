import math

a, b = map(int, input().split())
c, d = map(int, input().split())

n, m = a*d + c*b, b*d

while math.gcd(n,m) != 1 :
    a = math.gcd(n,m)
    n = int(n/a)
    m = int(m/a)
    
print(n, m)