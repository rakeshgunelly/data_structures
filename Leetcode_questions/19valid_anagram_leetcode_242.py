# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = Counter(s)
        y = Counter(t)
        
        if len(s)==len(t):
            for i in x:
                if x[i]!=y[i]:
                    return False
            return True
        
        return False
            

#more run time and space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)