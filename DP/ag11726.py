n = int(input())
lst = [0, 1, 2]
for i in range(3, 1001):
    lst.append(lst[i - 1] + lst[i - 2])
print(lst[n])