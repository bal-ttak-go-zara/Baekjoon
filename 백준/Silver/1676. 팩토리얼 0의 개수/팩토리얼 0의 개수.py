from math import factorial

n = str(factorial(int(input())))
cnt = 0

for i in reversed(n) :
    if i == '0' :
        cnt += 1

    else :
        break

print(cnt)
