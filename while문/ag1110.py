sol = int(input())
a = sol // 10
b = sol % 10
i = 1
while True:
    c = a + b
    x = b * 10 + c % 10
    
    if x == sol:
        print(i)
        break
    else:
        i = i + 1
        a = x // 10
        b = x % 10