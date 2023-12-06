memo = {}

def apt(floor, ho) :
    result = 0
    if floor*100+ho in memo :
        return memo[floor*100+ho]
    
    if floor == 0 :
        result = ho
        memo[ho] = result
        return result
    
    else :
        result = sum([apt(floor-1, ho-i) for i in range(ho)])
        memo[floor*100+ho] = result
        return result
        

for _ in range(int(input())) :
    k = int(input())
    n = int(input())
    
    print(apt(k,n))