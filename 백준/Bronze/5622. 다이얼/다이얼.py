a = input()
sec = 0
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

a = list(a)
for s in a :
    if s == 'S' :
        sec += 8
        continue
    if s == 'V' :
        sec += 9
        continue
    if s == 'Y' or s == 'Z' :
        sec += 10
        continue
    sec = sec + 3 + alphabet.index(s)//3

print(sec)
    