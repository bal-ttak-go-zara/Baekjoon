import itertools
n, m = map(int, input().split())
numlst = list(range(1,n+1))
lst = list(itertools.combinations(numlst, m))
for i in lst :
    i = list(i)
    for j in range(len(i)) :
        print(i[j], end = ' ')
    print()