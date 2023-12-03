p, w = map(int, input().split())
word = list(input())
sec = 0
before = -1

alphabet = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
    
for a in word :
    if alphabet.index(a) <= 14 :
        sec += (alphabet.index(a)%3+1)*p
    elif 14 < alphabet.index(a) <= 18 :
        sec += (alphabet.index(a)-14)*p
    elif 18 < alphabet.index(a) <= 21 :
        sec += (alphabet.index(a)-18)*p
    elif 21 < alphabet.index(a) <= 25 :
        sec += (alphabet.index(a)-21)*p
    elif alphabet.index(a) == 26 :
        sec += p

    if alphabet.index(a)//3 == before//3 and alphabet.index(a) <= 14 and before <= 14 :
        sec += w
    elif 15 <= alphabet.index(a) <=18 and 15 <= before <= 18 :
        sec += w
    elif 18 < alphabet.index(a) <= 21 and 18 < before <= 21 :
        sec += w
    elif 21 < alphabet.index(a) <= 25 and 21 < before <= 25 :
        sec += w
        
    before = alphabet.index(a)

print(sec)