def d(n):
    num = 0
    for i in list(str(n)):
        num = num + int(i)
    return num + n
lst = []
for i in range(1, 10001):
    lst.append(d(i))
set(lst)
for i in range(1, 10001):
    if i in lst:
        pass
    else:
        print(i)