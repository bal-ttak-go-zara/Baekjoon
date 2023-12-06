import sys

n = int(input())
dic = {key : 0 for key in sys.stdin.readline().split()}
m = int(input())

for i in sys.stdin.readline().split() :
    try :
        if dic[i] == 0 :
            print(1)

    except :
        print(0)