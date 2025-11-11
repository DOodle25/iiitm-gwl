n = 4  
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
adj_matrix[0][1] = 1
adj_matrix[0][2] = 1
adj_matrix[1][0] = 1
adj_matrix[2][0] = 1
adj_matrix[1][3] = 1
adj_matrix[1][2] = 1
adj_matrix[3][2] = 1
adj_matrix[3][1] = 1
adj_matrix[2][1] = 1
adj_matrix[2][3] = 1
print('    ', end='')
for i in range(n):
    print([i], end='')
print('')
for i, row in enumerate(adj_matrix):
    print([i],row)
def bfs(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n
    queue = []
    visited[start] = True
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for i in range(n):
            if adj_matrix[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)
def dfs(adj_matrix, start, visited=None):
    if visited is None:
        visited = [False] * len(adj_matrix)

    visited[start] = True
    print(start, end=' ')

    for i in range(len(adj_matrix)):
        if adj_matrix[start][i] == 1 and not visited[i]:
            dfs(adj_matrix, i, visited)
print("BFS starting from vertex 0:")
bfs(adj_matrix, 0)
print("\nDFS starting from vertex 0:")
dfs(adj_matrix, 0)