x = int(input())
i = 0

while x > i**2/2 + i/2 :
    i += 1

a = int(x-i**2/2 + i/2)

if i % 2 == 0 :
    print(f"{a}/{i-a+1}")
    
else :
    print(f"{i-a+1}/{a}")