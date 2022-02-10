# N-Repeated Element in Size 2N Array

# You are given an integer array nums with the following properties:

# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.

 

# Example 1:

# Input: nums = [1,2,3,3]
# Output: 3
# Example 2:

# Input: nums = [2,1,2,5,3,2]
# Output: 2
# Example 3:

# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5
 

# Constraints:

# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 104
# nums contains n + 1 unique elements and one of them is repeated exactly n times.

class Solution:
    def repeatedNTimes(self, nums):
        d = {}
        
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for key,values in d.items():
            if d[key]>1:
                return key
        
from random import random
class Solution:        
    def repeatedNTimes(self, A):
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]

from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums):
        d = defaultdict(int)
        
        for num in nums:
            if num in d.keys():
                return num
            else:
                d[num] =1