#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        l,r = 0,len(nums) - 1
        map = {}
        while l <= r:
            if nums[l] not in map:
                map[nums[l]] = 1
            else:
                map[nums[l]] += 1
            if nums[r] not in map and r != l:
                map[nums[r]] = 1
            elif nums[r] in map and r != l:
                map[nums[r]] += 1
            l += 1
            r -= 1
        for value in map:
            if map[value] == 1:
                return value
            
        
        
        
# @lc code=end

