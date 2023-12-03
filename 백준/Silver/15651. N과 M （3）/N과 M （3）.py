from itertools import product
n,m = map(int, input().split())
n_lst = list(range(1,n+1))

ans = list(product(n_lst, repeat=m))

for i in ans :
    print(*i)