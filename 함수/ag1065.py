N = int(input())
def f(n):
    sum = 0
    lst = []
    for i in range(1, n + 1):
        if i < 100:
            sum = sum + 1
        else:
            if ((i //10) %10) * 2 == i % 10 + i // 100 :
                sum = sum + 1
    return sum
print(f(N))