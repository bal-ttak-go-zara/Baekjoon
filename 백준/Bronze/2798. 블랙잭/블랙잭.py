import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
n = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for i in range(len(n)-2) :
    for j in range(i+1, len(n)-1) :
        for k in range(j+1, len(n)) :
            if m >= n[i]+n[j]+n[k] and (n[i]+n[j]+n[k])-ans > 0 :
                ans = n[i]+n[j]+n[k]

print(ans)