# Question 5
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Example 1:
# Input: nums = [1,2,3]
# Output: 6

def maximumProduct(nums):
    nums.sort()
    max_product = nums[-1] * nums[-2] * nums[-3]
    alternate_product = nums[0] * nums[1] * nums[-1]
    return max(max_product, alternate_product)

# Example usage:
nums = [1, 2, 3]
print(maximumProduct(nums))  # Output: 6
