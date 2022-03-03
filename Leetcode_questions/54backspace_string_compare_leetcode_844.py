# Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            ans = []
            
            for c in string:
                if c !='#':
                    ans.append(c)
                elif ans:
                    ans.pop()
                    
            return "".join(ans)
        return build(s)==build(t)
            
            
from functools import reduce
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def back(res,c):
            if c!="#":res.append(c)
            elif res: res.pop()
            return res
        return reduce(back,s,[])==reduce(back,t,[])
            
            
            
