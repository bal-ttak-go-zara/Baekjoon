test_case = int(input())

for i in range(test_case) :
    students = int(input())
    stu_num = []
    
    for j in range(students) :
        stu_num.append(int(input()))

    x = 0
    while True :
        div = []
        x += 1
        for k in range(students) :
            div.append(stu_num[k]%x)
        div = set(div)
        if len(div) == students :
            break
            
    print(x)