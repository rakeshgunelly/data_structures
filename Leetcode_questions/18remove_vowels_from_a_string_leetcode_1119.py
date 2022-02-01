# Remove Vowels from a String

# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

# Example 1:

# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:

# Input: s = "aeiou"
# Output: ""
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of only lowercase English letters.


import re
class Solution:
    def removeVowels(self, s: str) -> str:
        return re.sub("[aeiouAEIOU]","",s)
        
        
        
class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a','e','o','i','u']
        result = ''
        
        for i in s:
            if i  in vowels:
                continue
        
            result += i
                
        return result