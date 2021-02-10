import sys
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(str, sys.stdin.readline().split())
upper = 0
B = int(B)
sol = 0
for i in N[::-1]:
    sol = sol + arr.index(i) * (B**upper)
    upper += 1
print(sol)