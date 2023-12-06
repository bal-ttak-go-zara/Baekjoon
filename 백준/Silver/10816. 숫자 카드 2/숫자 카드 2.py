import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))

dic = {}

for _ in range(len(card)) :
    a = card.pop()
    if a in dic :
        dic[a] += 1
    else :
        dic[a] = 1

m = int(input())
find = list(map(int, sys.stdin.readline().split()))

for num in find :
    if num in dic :
        print(dic[num], end = ' ')
    else :
        print(0, end= ' ')