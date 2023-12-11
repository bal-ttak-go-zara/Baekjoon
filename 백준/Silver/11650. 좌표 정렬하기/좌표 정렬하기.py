import sys

dic = {}
for _ in range(int(input())) :
    x, y = map(int, sys.stdin.readline().split())
    if x in dic :
        dic[x].append(y)
    else :
        dic[x] = list()
        dic[x].append(y)

for i in sorted(dic.keys()) :
    for j in sorted(dic[i]) :
        print(i, j)