# Class Array
class Array():
    # Array initialization
    def __init__(self):
        self.Array = [int(i) for i in (str(input())).split()]
    # Largest_subarray_sum method to findout the largest array sum in time complexity n
    def Largest_subarray_sum(self):
        if not self.Array:
            return float('-inf')
        if len(self.Array) == 1:
            return self.Array[0]
        max_sum = self.Array[0]
        curr_sum = self.Array[0]
        for i in range(1, len(self.Array)):
            curr_sum = max(self.Array[i], curr_sum + self.Array[i])
            max_sum = max(curr_sum, max_sum)
        return max_sum
    
# Usage
array = Array()
print(array.Largest_subarray_sum())