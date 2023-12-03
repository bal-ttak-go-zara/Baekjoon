case = int(input())
for _ in range(case) :
    rep, code = input().split()
    for a in code :
        print(a*int(rep), end='')
    print()