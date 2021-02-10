inp = input()
sum = 0
for i in inp:
    if ord(i) >= 65 and ord(i) < 68:
        sum = sum + 3
    elif ord(i) >= 68 and ord(i) < 71:
        sum = sum + 4
    elif ord(i) >= 71 and ord(i) < 74:
        sum = sum + 5
    elif ord(i) >= 74 and ord(i) < 77:
        sum = sum + 6
    elif ord(i) >= 77 and ord(i) < 80:
        sum = sum + 7
    elif ord(i) >= 80 and ord(i) < 84:
        sum = sum + 8
    elif ord(i) >= 84 and ord(i) < 87:
        sum = sum + 9
    elif ord(i) >= 87 and ord(i) < 91:
        sum = sum + 10
    else:
        sum = sum + 11
print(sum)