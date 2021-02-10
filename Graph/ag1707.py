import sys
from collections import deque

k = int(sys.stdin.readline())

def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

for i in range(k):
    v, e = map(int, sys.stdin.readline().split())
    IsTrue = 1
    s = [[] for i in range(v + 1)]
    bi = [0 for i in range(v + 1)]
    for j in range(e):
        a, b = map(int, sys.stdin.readline().split())
        s[a].append(b)
        s[b].append(a)
    for k in range(1, v + 1):
        if bi[k] == 0:
            if not bfs(k):
                IsTrue = False
    print("YES" if IsTrue else "NO")