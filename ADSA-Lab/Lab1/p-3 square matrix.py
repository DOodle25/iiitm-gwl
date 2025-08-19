def printmatrix(matrix):
    for row in matrix:
        print(" ".join(row))
def printtruefalsematrix(matrix):
    print("visited matrix")
    for row in matrix:
        print("   ".join("1" if cell else "0" for cell in row))

with open("ADSA-Lab/Lab1/p3.txt") as f:
    matrix = [line.strip().split() for line in f if line.strip()]
printmatrix(matrix)
print(matrix)
n = len(matrix)

visited = [[False]*n for _ in range(n)]
printtruefalsematrix(visited)

blocks = 0
for i in range(n):
    for j in range(n):
        # print(i,j)
        # print(visited[i][j] ,matrix[i][j])
        if not visited[i][j] and matrix[i][j] == '1':
            blocks += 1
            # print(blocks, i,j)
            stack = [(i, j)]
            visited[i][j] = True
            # printtruefalsematrix(visited)
            while stack:
                # print(stack)
                x, y = stack.pop()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] == '1':
                        visited[nx][ny] = True
                        stack.append((nx, ny))

print(f"Number of blocks: {blocks}")
printmatrix(matrix)
printtruefalsematrix(visited)

