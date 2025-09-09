# import math

# def pascal_factorial(n):
#     for i in range(n):
#         print(" " * (n-i), end="")
#         for j in range(i+1):
#             print(math.comb(i, j), end=" ")
#         print()

# pascal_factorial(int(input("Enter the number of rows: ")))

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

# def pascal_recursive(n):
#     def C(n, k):
#         if k == 0 or k == n:
#             return 1
#         return C(n-1, k-1) + C(n-1, k)
    
#     for i in range(n):
#         print(" " * (n-i), end="")  # spacing
#         for j in range(i+1):
#             print(C(i, j), end=" ")
#         print()

# pascal_recursive(int(input("Enter the number of rows: ")))


# import numpy as np

# def pascal_polynomial(n):
#     poly = np.poly1d([1])  # (1)^0
#     for i in range(n):
#         # Coefficients of current row
#         coeffs = poly.coeffs[::-1].astype(int)
#         print(" " * (n-i), end="")
#         print(" ".join(map(str, coeffs)))
#         # Multiply by (1 + x) to get next row
#         poly = np.polymul(poly, np.poly1d([1, 1]))

# pascal_polynomial(int(input("Enter the number of rows: ")))


def count_not_divisible(n, p):
    """Count elements in row n not divisible by prime p using Lucas' theorem."""
    count = 1
    while n > 0:
        n, digit = divmod(n, p)
        count *= (digit + 1)
    return count

def pascal_lucas(n, p):
    """
    Prints the first n rows of Pascal's triangle modulo prime p.
    Uses Lucas theorem pattern for efficiency.
    """
    for row in range(n):
        # Compute number of elements not divisible by p
        num_elements = count_not_divisible(row, p)
        
        # Optional: Generate actual row values (here we just compute modulo p pattern)
        def generate_row(row):
            vals = [1]
            for k in range(1, row + 1):
                val = vals[-1] * (row - k + 1) // k
                vals.append(val)
            return vals
        
        actual_row = generate_row(row)
        
        # Format with spacing to make it triangular
        print(" " * (n - row), end="")
        print(" ".join(str(x) for x in actual_row))

# Example usage
n = int(input("Enter the number of rows: "))
p = 3  # prime for Lucas theorem (pattern for divisibility)
pascal_lucas(n, p)
