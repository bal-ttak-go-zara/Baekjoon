case = ''
mo =  ['a','e','i','o','u']

while True :
    cont = False
    case = input()
    case_org = case
    
    if case == 'end' :
        break
    
    for i in range(len(case)-1) :
        if case[i] == case[i+1] and case[i] != 'e' and case[i] != 'o' :
            print(f'<{case_org}> is not acceptable.')
            cont = True
            break
    if cont == True :
        continue
    

    if any(char in case for char in mo) == False :
        print(f'<{case_org}> is not acceptable.')
        continue
    

    for a in case :
        if a in mo :
            case = case.replace(a, '1')

        elif a != '1' or a != '0' :
            case = case.replace(a, '0')
    
    
    if '111' in case or '000' in case :
        print(f'<{case_org}> is not acceptable.')
        continue

    print(f'<{case_org}> is acceptable.')