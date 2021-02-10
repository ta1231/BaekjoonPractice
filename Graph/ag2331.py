import sys

a, p = map(int, sys.stdin.readline().split())
lst = [a]
while True:
    addNum = 0
    t = lst[-1]
    while t != 0:
        addNum += ((t%10) ** p)
        t //= 10
    if addNum in lst:
        print(lst.index(addNum))
        break
    else:
        lst.append(addNum)
            