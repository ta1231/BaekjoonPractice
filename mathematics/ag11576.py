A, B = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
ten = 0
upper = 0
for i in lst[::-1]:
    ten = ten + i*(A**upper)
    upper += 1
sol = []
while True:
    sol.append(ten % B)
    ten = ten // B
    if ten == 0:
        break
for i in sol[::-1]:
    print(i,end = " ")
