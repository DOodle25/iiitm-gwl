while True:
    r = 0
    n = int(input("Enter number of processes: "))
    for i in range(1, n + 1):
        for j in range(i - 1, n + 1):
            for k in range(i + j - 1, n + 1):
                r += 1
    print(r)