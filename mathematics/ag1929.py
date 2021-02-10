M, N = map(int, input().split())
def isPrimary(x):
    if x == 1:
        return 0
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return 0
    return x


for i in range(M, N + 1):
    if isPrimary(i) != 0:
        print(i)
    else:
        continue