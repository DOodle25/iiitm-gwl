def pushCar(stack, val):
    stack.append(val)
def popCar(stack):
    return stack.pop()
p1 = []
p2 = []
pushCar(p1, 1)
pushCar(p1, 2)
pushCar(p1, 3)
pushCar(p1, 4)
pushCar(p1, 5)
while p1:
    pushCar(p2, popCar(p1))
print(p1, p2)

# draw the state of s1 and s2 after each move
# p1: 1 2 3 4 5
# p2: 
# p1: 1 2 3 4 
# p2: 5
# p1: 1 2 3 
# p2: 5 4
# p1: 1 2 
# p2: 5 4 3
# p1: 1 
# p2: 5 4 3 2
# p1: 
# p2: 5 4 3 2 1

# at the end, list the final order of cars in s2(from top to bottom)
# 5 4 3 2 1

# Explain whether the cars in s2 are in the same order as they arrived or in the reverse order 
# reverse