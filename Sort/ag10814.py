import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(list(map(str, sys.stdin.readline().split())))
lst.sort(key = lambda x: [int(x[0])])
for i in lst:
    print(i[0], i[1])