
# def pascal_iterative(n):
#     triangle = []
#     for i in range(n):
#         row = [1] * (i + 1)
#         for j in range(1, i):
#             row[j] = triangle[i-1][j-1] + triangle[i-1][j]
#         triangle.append(row)
    
#     for i, row in enumerate(triangle):
#         print(" " * (n-i), end="")
#         print(" ".join(map(str, row)))

# pascal_iterative(int(input("Enter the number of rows: ")))
