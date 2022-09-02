#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        currSum = 0
        for num in nums:
            currSum+=num
            ans.append(currSum)
        return ans
# @lc code=end

