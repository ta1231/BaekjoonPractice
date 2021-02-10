arr = 'abcdefghijklmnopqrstuvwxyz'
lst = [-1] * 26
inp = input()
temp = 0
for i in range(len(inp)):
    if lst[arr.index(inp[i])] != -1:
        continue
    lst[arr.index(inp[i])] = i
for i in range(len(lst)):
    print(lst[i], end = ' ')