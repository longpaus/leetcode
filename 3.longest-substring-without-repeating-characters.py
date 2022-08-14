#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        longest = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[i])
            if longest < len(charSet):
                longest = len(charSet)
        return longest

        
# @lc code=end

