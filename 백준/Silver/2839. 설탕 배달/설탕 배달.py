n = int(input())

if n == 3 :
    print(1)

elif n == 4:
    print(-1)

else :
    if n%5 == 0 :
        print(n//5)

    elif n%5 == 1 :
        print((n//5-1) + 2)

    elif n%5 == 2 :
        if n//5 < 2 :
            print(-1)
        else :
            print((n//5-2) + 4)

    elif n%5 == 3 :
        print(n//5+1)

    else :
        print((n//5-1) + 3)