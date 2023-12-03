n = list(range(1, int(input())+1))

while len(n) != 1 :
    if len(n)%2 == 0 :
        n = list([n[x] for x in range(1, len(n), 2)])

    else :
        a = n.pop(-1)
        n = list([n[x] for x in range(1, len(n), 2)])
        n.insert(0, a)

print(n[0])