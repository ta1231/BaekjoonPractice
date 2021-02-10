import sys
lst = list(map(str, sys.stdin.readline().split()))
front = lst[0]+lst[1]
rear = lst[2]+lst[3]
print(int(front) + int(rear))