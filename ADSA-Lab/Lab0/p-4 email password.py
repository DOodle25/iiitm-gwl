email = None
password = None

email = str(input("Enter the Email:"))
flag = 0
for i in email:
    if str(i) == "@":
        if flag == 1:
            flag += 1
        flag += 1
    if str(i) == "." and flag == 1:
        flag += 1
if flag == 2:
    print("correct email")
password = str(input("Enter Password:"))

if len(password) >= 8:
    print("correct password")
else:
    print("wrong password")