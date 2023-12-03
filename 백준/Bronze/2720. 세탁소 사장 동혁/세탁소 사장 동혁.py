time = int(input())
money = []
cent = [25,10,5,1]

for i in range(time) :
    money.append(int(input()))

for m in money :
    for c in cent :
        print(m//c, end=' ')
        m = m - (m//c)*c
    print()