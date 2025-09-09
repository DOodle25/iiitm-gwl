while True:
    n = int(input("Enter a number: "))
    r= 0 
    for i in range(1,n+1):
        for j in range(1,2*i + 1):
            k = j
            while k >= 0:
                r += 1
                k -= 1
    print(r)
