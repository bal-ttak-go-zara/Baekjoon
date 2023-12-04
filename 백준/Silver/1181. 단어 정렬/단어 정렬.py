lst = []
for _ in range(int(input())) :
    lst.append(input())

lst = set(lst)
lst = sorted(lst, key=lambda x : (len(x), x))

for n in lst :
    print(n)