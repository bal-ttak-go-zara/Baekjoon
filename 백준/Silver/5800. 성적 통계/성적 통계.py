k = int(input())

for i in range(k) :
    st_num_scr = list(map(int, input().split()))
    st_num = st_num_scr[0]
    st_num_scr.pop(0)

    st_num_scr = sorted(st_num_scr, reverse = True)

    var = []

    for j in range(len(st_num_scr)-1) :
        var.append(st_num_scr[j]-st_num_scr[j+1])
    var = sorted(var, reverse = True)
        
    print(f"Class {i+1}")
    print(f"Max {st_num_scr[0]}, Min {st_num_scr[-1]}, Largest gap {var[0]}")