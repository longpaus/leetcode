#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j]:
                    total += 1
        return total
        
# @lc code=end

