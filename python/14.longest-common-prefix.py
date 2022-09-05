#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from pickle import FALSE


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)==1:
            return strs[0]
        prefix = ""
        finished = False
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i > len(strs[j]) - 1 or strs[j][i] != strs[0][i]:
                    finished = True
            if finished:
                break
            prefix += strs[0][i]
        return prefix
                

        
# @lc code=end

