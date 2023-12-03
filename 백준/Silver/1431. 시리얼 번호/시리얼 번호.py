dic = {}
for _ in range(int(input())) :
    a = input()
    dic[a] = 0
    for n in a :
        try :
            dic[a] += int(n)
        except :
            continue
            
for i in sorted(dic.keys(), key = lambda x : (len(x), dic[x], x)) :
    print(i)