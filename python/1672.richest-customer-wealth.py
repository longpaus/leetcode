#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for account in accounts:
            if sum(account) > richest:
                richest = sum(account)
        return richest
        
# @lc code=end

