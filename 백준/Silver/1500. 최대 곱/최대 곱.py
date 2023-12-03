a, b = map(int, input().split())
lst = [a//b for _ in range(b)]
left = a%b
for i in range(left) :
    lst[i] += 1

ans = 1
for j in range(b) :
    ans *= lst[j]

print(ans)