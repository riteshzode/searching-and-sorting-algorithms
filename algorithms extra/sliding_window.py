# Solution 1: Sliding Window Optimized Approach
def find_max_average_1(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum / k)
    return max_sum


# Solution 2: Sliding Window Approach 2
def find_max_average_2(nums, k):
    start = 0
    max_sum = float('-inf')
    window_sum = 0
    for end in range(len(nums)):
        window_sum += nums[end]
        if end - start + 1 == k:
            max_sum = max(max_sum, window_sum / k)
            window_sum -= nums[start]
            start += 1
    return max_sum


# Solution 3: Sliding Window Approach 3
def find_max_average_3(nums, k):
    max_sum = 0
    for i in range(len(nums)):
        window_sum = 0
        for j in range(k):
            if i + k - 1 < len(nums):
                window_sum += nums[i + j]
            else:
                i = len(nums)
                j = k
        max_sum = max(max_sum, window_sum / k)
    return max_sum

# nums = [1, 12, -5, -6, 50, 3]
# k = 4
#
# max_average_1 = find_max_average_1(nums, k)
# max_average_2 = find_max_average_2(nums, k)
# max_average_3 = find_max_average_3(nums, k)
#
# print("Solution 1: Maximum Average = ", max_average_1)
# print("Solution 2: Maximum Average = ", max_average_2)
# print("Solution 3: Maximum Average = ", max_average_3)
