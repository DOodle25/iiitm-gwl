def largest_sum_subarray_n_squared(arr):
    n = len(arr)
    max_sum = float('-inf')
    start, end = 0, 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j

    return max_sum, start, end

arr = [-2,1,-3,4,-1,2,1,-5,4]
print("O(n^2) approach:", largest_sum_subarray_n_squared(arr))




























# def largest_sum_subarray_nlogn(arr):
#     def max_crossing_sum(arr, left, mid, right):
#         left_sum = float('-inf')
#         total = 0
#         for i in range(mid, left - 1, -1):
#             total += arr[i]
#             if total > left_sum:
#                 left_sum = total

#         right_sum = float('-inf')
#         total = 0
#         for i in range(mid + 1, right + 1):
#             total += arr[i]
#             if total > right_sum:
#                 right_sum = total

#         return left_sum + right_sum

#     def max_subarray_sum(arr, left, right):
#         if left == right:
#             return arr[left]

#         mid = (left + right) // 2
#         return max(max_subarray_sum(arr, left, mid),
#                    max_subarray_sum(arr, mid + 1, right),
#                    max_crossing_sum(arr, left, mid, right))

#     return max_subarray_sum(arr, 0, len(arr) - 1)

# def largest_sum_subarray_n(arr):
#     max_so_far = arr[0]
#     max_ending_here = arr[0]
#     start = end = s = 0

#     for i in range(1, len(arr)):
#         if arr[i] > max_ending_here + arr[i]:
#             max_ending_here = arr[i]
#             s = i
#         else:
#             max_ending_here += arr[i]

#         if max_ending_here > max_so_far:
#             max_so_far = max_ending_here
#             start = s
#             end = i

#     return max_so_far, start, end

# Example usage:

# print("O(n log n) approach:", largest_sum_subarray_nlogn(arr))
# print("O(n) approach:", largest_sum_subarray_n(arr))