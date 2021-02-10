# n, m = map(int, input().split())
# s = []
# queue = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# for i in range(n):
#     s.append(list(map(int, input())))
# queue = [[0, 0]]
# s[0][0] = 1
# while queue:
#     a, b = queue[0][0], queue[0][1]
#     del queue[0]
#     for i in range(4):
#         x = a + dx[i]
#         y = b + dy[i]
#         if 0 <= x < n and 0 <= y < m and s[x][y] == 1:
#             queue.append([x, y])
#             s[x][y] = s[a][b] + 1
# print(s[n - 1][m - 1])

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input())))
queue = [[0, 0]]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:   # 범위안에 있고 새로운 좌표가 1일 때
            queue.append([nx, ny])   # 새로운 좌표를 큐에 추가한다
            matrix[nx][ny] = matrix[x][y] + 1

print(matrix[n - 1][m - 1])
