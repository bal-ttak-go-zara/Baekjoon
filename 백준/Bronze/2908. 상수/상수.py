a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()
if a[0] > b[0] :
    for num in a :
        print(num, end='')
elif b[0] > a[0] :
    for num in b :
        print(num, end='')
else :
    if a[1] > b[1] :
        for num in a :
            print(num, end='')
    elif b[1] > a[1] :
        for num in b :
            print(num, end='')
    else :
        if a[2] > b[2] :
            for num in a :
                print(num, end = '')
        else :
            for num in b :
                print(num, end = '')