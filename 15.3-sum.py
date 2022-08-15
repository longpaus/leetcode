#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for f in range(len(nums) - 1):
            l = f + 1
            r = len(nums) - 1
            while l < r:
                if nums[f] + nums[l] + nums[r] == 0:
                    answer.append([nums[f],nums[l],nums[r]])
                    l += 1
                elif nums[f] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[f] + nums[l] + nums[r] < 0:
                    l += 1
        return list(set(tuple((sub)) for sub in answer))
# @lc code=end

