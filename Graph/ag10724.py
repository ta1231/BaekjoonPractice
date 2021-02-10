import sys
tc = int(sys.stdin.readline())

for i in range(tc):
    cnt = 0
    def dfs(i):
        visit[i] = 1
        for k in range(s + 1):
            if matrix[i][k] == 1 and visit[k] == 0:
                dfs(k)
    s = int(input())
    matrix = [[0] *(s + 1) for i in range(s + 1)]
    visit = [0] * (s + 1)
    line = list(map(int, sys.stdin.readline().split()))
    for i in range(1, s + 1):
        matrix[i][line[i - 1]] = matrix[line[i - 1]][i] = 1
    for i in range(1, s + 1):
        if visit[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)