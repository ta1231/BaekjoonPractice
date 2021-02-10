import sys
inp = sys.stdin.readline().rstrip()
lst = []
n = len(inp)
for i in range(n):
    lst.append(inp)
    inp = inp[1:]
for i in sorted(lst):
    print(i)