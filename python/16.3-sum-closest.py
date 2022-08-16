#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        closest = nums[0] + nums[1] + nums[2]
        for f in range(len(nums) - 2):
            l = f + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[f] + nums[l] + nums[r]
                if abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return threeSum
        return closest
        
        
# @lc code=end

