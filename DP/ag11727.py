n = int(input())
lst = [0] * (1001)
lst[0] = 0
lst[1] = 1
lst[2] = 3
for i in range(3, 1001):
    lst[i] = 2*lst[i - 2] + lst[i - 1]
print(lst[n] % 10007)