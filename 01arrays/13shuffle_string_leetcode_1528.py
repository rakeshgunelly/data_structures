# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

 

# Example 1:


# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:

# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.
 

# Constraints:

# s.length == indices.length == n
# 1 <= n <= 100
# s consists of only lowercase English letters.
# 0 <= indices[i] < n
# All values of indices are unique.

# Time Submitted     Status      Runtime    Memory      Language
# 01/03/2022 21:38	 Accepted	 87 ms	    14.2 MB	    python3
class Solution:
    def restoreString(self, s, indices):
        result = [0]*len(indices)
        resultString = ''
        
        for i in range(len(indices)):
            result[indices[i]]=s[i]
        
        for i in result:
            resultString += i
            
        return resultString


# Time Submitted      Status      Runtime     Memory      Language
# 01/03/2022 21:45	Accepted	52 ms	    14.3 MB	    python3



# Solution with string methods
class Solution:
    def restoreString(self, s, indices):
        ans=['']*len(s)
        for i,j in enumerate(s):
            ans[indices[i]]=j
        return ''.join(ans)