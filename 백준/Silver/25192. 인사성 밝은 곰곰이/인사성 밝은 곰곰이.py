import sys
cnt = 0

for _ in range(int(input())) :
    a = sys.stdin.readline().rstrip()

    if a == 'ENTER' :
        dic = {}
        continue

    if a not in dic :
        dic[a] = 1
        cnt += 1

print(cnt)