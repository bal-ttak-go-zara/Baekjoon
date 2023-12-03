n, m = map(int, input().split()) # n = 끊어진 기타줄 수, m = 브랜드 개수
price = []

def six_price(lst) :
    for idx in range(len(lst)) :
        if idx % 2 == 1 :
            lst[idx] = lst[idx] * 6

    return min(lst) * (n//6)


def left_price(lst, left) :
    for idx in range(len(lst)) :
        if idx % 2 == 1 :
            lst[idx] = int(lst[idx] / 6) * left

    return min(lst)



for _ in range(m) :
    price.extend(map(int, input().split()))
    

if n % 6 == 0 :
    print(six_price(price))
else :
    print(six_price(price) + left_price(price, n%6))