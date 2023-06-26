# Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5

from collections import defaultdict

def findLHS(nums):
    num_count = defaultdict(int)
    for num in nums:
        num_count[num] += 1
    max_length = 0
    for num in num_count:
        if num + 1 in num_count:
            max_length = max(max_length, num_count[num] + num_count[num + 1])
    return max_length

# Example usage:
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))  # Output: 5