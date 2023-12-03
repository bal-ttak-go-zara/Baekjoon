x = int(input())
n = []
lst = [64, 32, 16, 8, 4, 2, 1]

i = 0
while x != 0 :
    if x >= lst[i] :
        n.append(lst[i])
        x -= lst[i]
    i += 1

print(len(n))
