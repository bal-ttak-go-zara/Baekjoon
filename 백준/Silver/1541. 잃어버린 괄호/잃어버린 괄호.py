a = input().split('-')

if '+' in a[0] :
    s = list(map(int, a[0].split('+')))
    ans = sum(s)

else :
    ans = int(a[0])

for i in range(1, len(a)) :
    if '+' in a[i] :
        s = list(map(int, a[i].split('+')))
        a[i] = sum(s)
    
    ans -= int(a[i])
        
    
print(ans)