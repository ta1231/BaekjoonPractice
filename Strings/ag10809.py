inp = input()
arr = [-1] * 26
idx = 0
for i in inp:
    if arr[ord(i) - 97] == -1:
        arr[ord(i) - 97] = idx
        idx += 1
    else:
        idx += 1 
for i in arr:
    print(i, end = ' ')