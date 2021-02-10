N, M, V = map(int, input().split())
matrix = [[0] *(N + 1)for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visit_list = [0]*(N + 1)

def dfs(V):
    visit_list[V] = 1
    print(V, end= " ")
    for i in range(1, N + 1):
        if(visit_list[i] == 0 and matrix[V][i] == 1): #방문하지 않고 노드가 연결되어있으면
            dfs(i)

def bfs(V):
    queue = [V]
    visit_list[V] = 0 # 방문한 점 0으로 표시
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')
        for i in range(1, N+1):
            if(visit_list[i] == 1 and matrix[V][i] == 1): # 방문하지않고 노드끼리 연결되어있으면
                queue.append(i) # 큐에 추가
                visit_list[i] = 0 #방문한 점 0으로 표시

dfs(V)
print()
bfs(V)