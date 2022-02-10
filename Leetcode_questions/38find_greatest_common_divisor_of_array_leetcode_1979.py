# Find Greatest Common Divisor of Array

# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

# Example 1:

# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.
# Example 2:

# Input: nums = [7,5,6,8,3]
# Output: 1
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 8.
# The greatest common divisor of 3 and 8 is 1.
# Example 3:

# Input: nums = [3,3]
# Output: 3
# Explanation:
# The smallest number in nums is 3.
# The largest number in nums is 3.
# The greatest common divisor of 3 and 3 is 3.
 

# Constraints:

# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000

class Solution:
    def findGCD(self, nums):
        mx = max(nums)
        mn = min(nums)
        
        for i in range(mn,1,-1):
            if mx%i == 0 and mn%i==0:
                return i
        return 1