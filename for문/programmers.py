s = input()
for i in range(len(s)):
    if (ord(s[i])) >=49 and (ord(s[i])) <=58:
        continue
    else:
        print(False)
        break
