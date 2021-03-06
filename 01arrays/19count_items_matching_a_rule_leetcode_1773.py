# # 19count_items_matching_a_rule_leetcode_1773.py
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.

 

# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
# Example 2:

# Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
 

# Constraints:

# 1 <= items.length <= 104
# 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
# ruleKey is equal to either "type", "color", or "name".
# All strings consist only of lowercase letters.

# Time Submitted      Status      Runtime     Memory      Language
# 01/05/2022 11:46	Accepted	523 ms	    20.6 MB	    python3
class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        
        ruleKeys = ['type','color','name']
        ruleKeyIndex = 0
        count = 0
        
        for i in range(len(ruleKeys)):
            if ruleKey == ruleKeys[i]:
                ruleKeyIndex = i
                        
        for i in range(len(items)):
            if items[i][ruleKeyIndex] == ruleValue:
                count += 1
                
        return count
            


# Time Submitted      Status      Runtime     Memory      Language
# 01/05/2022 11:52	Accepted	451 ms	    20.4 MB	    python3

# using dictionaries 

class Solution:
    def countMatches(self, items, ruleKey: str, ruleValue: str) -> int:
        count=0
        dic={"color":1,"type":0,"name":2}
        for i in range(len(items)):
            if items[i][dic[ruleKey]]==ruleValue:
                count+=1
        return count