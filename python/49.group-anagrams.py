#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(lambda:[])
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res

        
# @lc code=end

