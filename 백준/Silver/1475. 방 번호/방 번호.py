n = list(input())
n_int = list(map(int, n))
many = []
ans = 0

for i in range(10) :
    many.append(n_int.count(i))


if many.index(max(many)) == 6 or many.index(max(many)) == 9 :
    a = (many[6] + many[9] + 1) // 2
    many[9] = a
    many[6] = a

ans = max(many)
print(ans)