n = int(input("enter number n:"))
flag = 0
if n == 1 or n == 2:
    print("prime")
else:
    for i in range(2,n//2 + 1):
        if n%i == 0:
            print("not prime")
            flag = 1
            break
    if not flag:
        print("prime")