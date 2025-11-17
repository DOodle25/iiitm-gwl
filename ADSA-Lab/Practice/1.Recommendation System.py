import random

# Recommendation System: Finding Maximum Subarray Sum using Different Algorithms


# Generate random user ratings (simulate recommendations)
def generate_ratings(n, low=-10, high=10):
    return [random.randint(low, high) for _ in range(n)]

# 1. Prefix Sum (O(n^2))
def max_subarray_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix[j+1] - prefix[i]
            max_sum = max(max_sum, curr_sum)
    return max_sum

# 2. Brute Force (O(n^3))
def max_subarray_brute_force(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j+1):
                curr_sum += arr[k]
            max_sum = max(max_sum, curr_sum)
    return max_sum

# 3. Kadane's Algorithm (O(n))
def max_subarray_kadane(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# 4. Divide and Conquer (O(n log n))
def max_crossing_sum(arr, left, mid, right):
    left_sum = float('-inf')
    sum_ = 0
    for i in range(mid, left-1, -1):
        sum_ += arr[i]
        left_sum = max(left_sum, sum_)
    right_sum = float('-inf')
    sum_ = 0
    for i in range(mid+1, right+1):
        sum_ += arr[i]
        right_sum = max(right_sum, sum_)
    return left_sum + right_sum

def max_subarray_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = max_subarray_divide_conquer(arr, left, mid)
    right_max = max_subarray_divide_conquer(arr, mid+1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)
    return max(left_max, right_max, cross_max)

# Example usage
if __name__ == "__main__":
    n = 10
    ratings = generate_ratings(n)
    print("User Ratings:", ratings)
    print("Max Subarray Sum (Prefix Sum O(n^2)):", max_subarray_prefix_sum(ratings))
    print("Max Subarray Sum (Brute Force O(n^3)):", max_subarray_brute_force(ratings))
    print("Max Subarray Sum (Kadane's O(n)):", max_subarray_kadane(ratings))
    print("Max Subarray Sum (Divide & Conquer O(n log n)):", max_subarray_divide_conquer(ratings, 0, n-1))