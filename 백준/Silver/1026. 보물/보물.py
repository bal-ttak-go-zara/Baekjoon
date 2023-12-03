n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_size = sorted(b, reverse = True)

for x in range(n) :
    b_size[x] = b.index(b_size[x])

a = sorted(a)
ans = 0
for y in range(n) :
    ans += a[y] * b[b_size[y]]

print(ans)