while True :
    n = str(input())
    if n == '0' :
        break

    if list(n) == list(reversed(n)) :
        print('yes')

    else :
        print('no')