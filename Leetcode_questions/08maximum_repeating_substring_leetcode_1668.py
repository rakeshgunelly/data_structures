# Maximum Repeating Substring

# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

# Given strings sequence and word, return the maximum k-repeating value of word in sequence.

 

# Example 1:

# Input: sequence = "ababc", word = "ab"
# Output: 2
# Explanation: "abab" is a substring in "ababc".
# Example 2:

# Input: sequence = "ababc", word = "ba"
# Output: 1
# Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
# Example 3:

# Input: sequence = "ababc", word = "ac"
# Output: 0
# Explanation: "ac" is not a substring in "ababc". 
 

# Constraints:

# 1 <= sequence.length <= 100
# 1 <= word.length <= 100
# sequence and word contains only lowercase English letters.



# class Solution:
#     def maxRepeating(self, sequence: str, word: str) -> int:
#         count = 0
#         i=0
        
#         while (i<=len(sequence)):
#             seq = sequence[i:i+len(word)]
#             if sequence[i:i+len(word)] == word:
#                 count +=1
#                 i = i+len(word)
#             else:
#                 i=i+1

#         # for i in range(len(sequence)):
#         #     seq = sequence[i:i+len(word)]
#         #     if seq==word:
#         #         count += 1
#         return count
        

# someSoultion = Solution()
# result = someSoultion.maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba")
# print(result)




class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        tmp = word
        ans = 0 
        while len(tmp) <= len(sequence): 
            
            if sequence.find(tmp) != -1: 
                tmp += word 
                ans += 1 
            else:
                return ans 
                
        return ans 
