import math

def find_rounds_to_meet(N, kim, lim):
    rounds = 1
    while N > 1:
        kim = (kim + 1) // 2
        lim = (lim + 1) // 2
        if kim == lim:
            return rounds
        rounds += 1
        N = math.ceil(N / 2)

N, kim, lim = map(int, input().split())
result = find_rounds_to_meet(N, kim, lim)
print(result)