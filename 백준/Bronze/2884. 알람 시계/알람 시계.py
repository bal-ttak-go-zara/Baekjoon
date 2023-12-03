h,m = map(int, input().split())
if m < 45 :
    m += 15
    print(h-1 if h != 0 else 23, end =' ')
    print(m)
else :
    m -= 45
    print(h, m)