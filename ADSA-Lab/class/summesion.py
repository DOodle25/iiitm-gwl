k = 0 
n = int(input("Enter the input size:"))
for i in range(n**2, n**2 + 2*n + 1):
    for j in range(1, n + i + 1):
        k += 1
        print(k)
print("value of k:", k)