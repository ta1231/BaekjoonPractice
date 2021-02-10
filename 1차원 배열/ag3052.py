lst = [0] * 42
sum = 0
for i in range(10):
    inp = int(input())
    inp = inp % 42
    lst[inp] = lst[inp] + 1
for i in range(len(lst)):
    if lst[i] != 0:
        sum = sum + 1
    else:
        continue
print(sum)
