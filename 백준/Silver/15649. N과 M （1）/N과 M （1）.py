import itertools
n,m = map(int, input().split())
n_lst = list(range(1,n+1))

for s in itertools.permutations(n_lst, m) :
    list(s)
    for i in s :
        print(i, end=' ')
    print()