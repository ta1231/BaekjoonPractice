N = int(input())
sum = 0
for i in range(1, N + 1):
    if i % 125 == 0:
        sum +=3
        continue
    elif i % 25 == 0:
        sum += 2
        continue
    elif i % 5 == 0:
        sum += 1
        continue
    else:
        continue
print(sum)
