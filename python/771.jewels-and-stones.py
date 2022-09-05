#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesMap = defaultdict(lambda:0)
        for stone in stones:
            stonesMap[stone] += 1
        res = 0
        for jewel in jewels:
            res += stonesMap[jewel]
        return res
        
# @lc code=end

