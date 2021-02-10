import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
id = [1]
for i in range(1, len(lst)):
    if lst[i] == lst[i - 1]:
        id[-1] += 1
    else:
        id.append(1)
lst = list(set(lst))
print(lst[id.index(max(id))])


