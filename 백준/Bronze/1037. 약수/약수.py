n = int(input())
num = list(map(int, input().split()))
num = sorted(num)
print(num[0]*num[n-1] if n%2==0 else num[int((n+1)/2)-1]**2)