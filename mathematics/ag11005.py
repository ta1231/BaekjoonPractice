import sys
N, B = map(int, sys.stdin.readline().split())
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sol = ''
while N != 0:
    a = N % B
    sol = array[a] + sol
    N = N // B
print(sol)
