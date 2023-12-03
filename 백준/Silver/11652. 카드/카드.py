dic = {}
for _ in range(int(input())) :
    num = int(input())
    if num not in dic :
        dic[num] = 1
    else :
        dic[num] += 1

dic = sorted(dic.keys(), key = lambda x : (dic[x], -x))
print(dic[-1])