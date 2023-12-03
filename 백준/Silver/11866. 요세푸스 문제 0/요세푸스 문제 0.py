n, k = map(int, input().split())
lst = list(range(1, n+1))

print('<', end='')

fst, cnt = 0, 0
while len(lst) != 1 :
    cnt += 1
    if cnt == k :
        print(f'{lst[0]}, ', end='')
        lst.remove(lst[0])
        cnt = 0
    else :
        fst = lst.pop(0)
        lst.append(fst)
    
    
print(f'{lst[0]}>')