ans = [1,1,2,2,2,8]
find = list(map(int,input().split()))
for i in range(6) :
    print(ans[i]-find[i], end=' ')