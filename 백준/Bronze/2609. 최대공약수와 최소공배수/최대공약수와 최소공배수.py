n, m = map(int, input().split())
lst = [[],[]]

for i in range(1, n+1) :
    if n/i == n//i :
        lst[0].append(i)

for j in range(1, m+1) :
    if m/j == m//j :
        lst[1].append(j)

print(max(set(lst[0])&set(lst[1])))

i, j = 1,1
while True :
    if n*i == m*j :
        print(n*i)
        break

    elif n*i > m*j :
        j += 1

    else :
        i += 1