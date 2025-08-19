def pushStack(stack, val):
    stack.append(val)
def popStack(stack):
    return stack.pop()
s1 = []
s2 = []
pushStack(s1, 3)
pushStack(s1, 5)
pushStack(s1, 7)
pushStack(s1, 9)
pushStack(s1, 11)
pushStack(s1 ,13)
while s1:
    pushStack(s2, popStack(s1))
print(s1, s2)