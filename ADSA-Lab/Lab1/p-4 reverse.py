def pushStack(stack, val):
    stack.append(val)
def popStack(stack):
    return stack.pop()

Array = [-1]*(int(input("Enter the size of the array: ")))
Array = list(map(int, input("Enter the array elements separated by space: ").split()))
print("Original Array:", Array)

stack = []
for i in Array:
    pushStack(stack, i)
print(stack)
for i in range(len(Array)):
    Array[i] = popStack(stack)

print("Reversed Array:", Array)

# Time complexity analysis:
# for i in array --> n
# for i in stack --> n
# time complexzity O(n)

# In-place reversal of array
for i in range(len(Array) // 2):
    Array[i], Array[-i - 1] = Array[-i - 1], Array[i]
print("In-place Reversed Array:", Array)