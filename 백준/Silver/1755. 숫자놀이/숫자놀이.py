m, n = map(int, input().split())

v_lst = ['8','5','4','9','1','7','6','3','2','0']
ans_dic = {}

for i in range(m, n+1) :
    v = str(i)
    i = list(str(i))
    i = list(map(lambda x : v_lst.index(x), i))
    
    ans_dic[v] = ''.join(map(str, i))

count = 0
for key in sorted(ans_dic.keys(), key = lambda k : ans_dic[k]) :
    count += 1
    print(key, end = ' ')
    if count%10 == 0 :
        print()