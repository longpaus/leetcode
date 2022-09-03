#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

# ahsdhabba
# baab

# aaaa


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            # odd length
            l,r = i,i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
            # even length
            l,r = i,i+1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r+1]
                l -= 1
                r += 1
        return longest
            

        


# @lc code=end
