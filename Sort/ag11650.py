N = int(input())
lst = []
for i in range(N):
    t = list(map(int, input().split()))
    lst.append(t)
for i in sorted(lst):
    print("{0} {1}".format(i[0], i[1]))