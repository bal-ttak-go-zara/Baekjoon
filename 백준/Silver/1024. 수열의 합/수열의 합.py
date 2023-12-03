n, l = map(int, input().split())

while True :
    if l > 100 :
        print('-1')
        break

    if l % 2 == 0 :
        if n % l == l/2 :
            if n//l+int(-l/2)+1 < 0 :
                print('-1')
                break
            
            for i in range(int(-l/2), int(l/2)) :
                print(n//l+i+1, end=' ')
            break
        
        else :
            l += 1

    else :
        if n % l == 0 :
            if n//l+int(-(l-1)/2) < 0 :
                print('-1')
                break
            
            for j in range(int(-(l-1)/2), int((l-1)/2)+1) :
                print(n//l+j, end = ' ')
            break

        else :
            l += 1
        