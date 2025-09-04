n = int(input("enter n:"))
i = 1
j = 1
for k in range(n-1):
    temp  = i + j
    i = j
    j = temp

print(i)