import sys 
A, B = map(int, sys.stdin.readline().split())
a, b = A, B 
while b != 0:
    a = a % b 
    a, b = b, a 
# 최소공약수
print(a) 
# 최소공배수
print(A*B//a)
