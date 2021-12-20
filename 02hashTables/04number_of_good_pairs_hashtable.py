class Solution:
    def numIdenticalPairs(self, nums):
        
        counter = 0
        dict = {}

        for i in nums:
            if i in dict:
                counter+=dict[i]
                dict[i]+=1
            else:
                dict[i]=1

        return counter

some = Solution()

print(some.numIdenticalPairs([1,2,3,1,1,3]))