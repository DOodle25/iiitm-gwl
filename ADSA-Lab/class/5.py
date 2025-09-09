import math
while True:
    n = int(input("Enter a number: "))
    r = 0
    for i in range(1, n*n ):
        for j in range(i + 1, n - math.ceil(math.sqrt(i)) + 1):
            for k in range(1, j+ 1):
                r += 1
    print(r)
