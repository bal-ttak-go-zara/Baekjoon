for _ in range(int(input())) :
    test = input()
    test = test.replace('(', 'a')
    test = test.replace(')', 'b')

    if len(test) % 2 == 1: #홀수면 VPS X
        print('NO')
        continue
    
    if test.count('a') != test.count('b') : #( ) 두 개 개수 다르면 VPS X
        print('NO')
        continue

    while 'ab' in test :
        test = test.replace('ab', '')

    if len(test) == 0 :
        print('YES')
    else :
        print('NO')