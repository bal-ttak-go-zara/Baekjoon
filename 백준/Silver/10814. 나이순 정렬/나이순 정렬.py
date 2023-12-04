import sys

dic = {}

for i in range(int(input())) :
    age, name = sys.stdin.readline().rstrip().split()
    dic[i] = [name, int(age), i]

for n in sorted(dic, key = lambda x : (dic[x][1], dic[x][2])) :
    print(dic[n][1], dic[n][0])