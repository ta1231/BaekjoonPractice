# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90
inp = input()
lst = [0] * 26
for i in inp:
    if ord(i) >= 65 and ord(i) <= 90:
        lst[ord(i) - 65] = lst[ord(i) - 65] + 1
    else:
        lst[ord(i) - 97] = lst[ord(i) - 97] + 1
maxOflst = max(lst)
comp = 0
sol = 0
for i in range(len(lst)):
    if lst[i] == maxOflst:
        comp = comp + 1
        sol = i
if comp > 1:
    print('?')
else:
    print(chr(65 + sol))

