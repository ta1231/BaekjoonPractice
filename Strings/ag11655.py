# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90
import sys
inp = sys.stdin.readline().rstrip()
sol = ''
for i in inp:
    if 97 <= ord(i) <= 109:
        sol += (chr(ord(i) + 13))
    elif 110 <= ord(i) <= 122:
        sol += (chr(ord(i) - 13))
    elif 65 <= ord(i) <= 77:
        sol += (chr(ord(i) + 13))
    elif 78 <= ord(i) <= 90:
        sol += (chr(ord(i) - 13))
    else:
        sol += i
print(sol)