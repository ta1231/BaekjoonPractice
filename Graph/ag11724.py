import sys
n, m = map(int, sys.stdin.readline().split())
s = [[0]*(n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a][b] = s[b][a] = 1
visit = [0] * (n + 1)

cnt = 0

def dfs(i):
    visit[i] = 1
    for k in range(1, n + 1):
        if s[i][k] == 1 and visit[k] == 0:
            dfs(k)

for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)