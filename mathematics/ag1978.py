N = int(input())
sol = 0
lst = list(map(int, input().split()))
def isPrimary(x):
    if x == 1:
        return 0
        
    for j in range(2, x):
        if x % j == 0:
            return 0
    return 1
for i in lst:
    sol += isPrimary(i)
print(sol)