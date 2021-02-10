A = int(input())
B = int(input())
C = int(input())

lst = [0] * 10
x = A * B * C
d = 10
while 1:
    add_num = x % d
    lst[add_num] = lst[add_num] + 1
    
    if x // d == 0:
        for i in lst:
            print(i)
        break
    else:
        x = x // d
