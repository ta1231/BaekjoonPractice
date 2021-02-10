dp = []
def isPrimary(x):
    if x == 1:
        return 0
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return 0
    return x


for i in range(2, 1000001):
    if isPrimary(i) != 0:
        dp.append(i)
    else:
        continue

print(dp)

# while True:
#     n = int(input())
#     if n == 0: break
#     else:
#         for i in range(len(dp)):
#             for j in range(i):



