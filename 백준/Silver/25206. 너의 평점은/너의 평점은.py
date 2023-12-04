import sys

dic = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0}
ans = 0
hakjum_hap = 0

for _ in range(20) :
    name, hakjum, score = sys.stdin.readline().rstrip().split()
    if score != 'P' :
        score = dic[score]
        ans += float(hakjum) * score
        hakjum_hap += float(hakjum)

print(ans/hakjum_hap)