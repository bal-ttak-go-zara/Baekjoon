n = int(input())
name = list(input())
a = ''
for _ in range(n-1) :
    a = list(input())
    for s in range(len(name)) :
        if name[s] == '?' :
            continue
        if name[s] != a[s] :
            name[s] = '?'

for s in name :
    print(s, end='')