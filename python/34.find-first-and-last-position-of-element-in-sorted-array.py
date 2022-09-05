#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted nums
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low,mid,high = 0,-1,len(nums) - 1
        targetExist = False
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                targetExist = True
                break
        if not targetExist:
            return [-1,-1]
        ans = [mid,mid]
        i = 1
        while mid - i >= 0 and nums[mid - i] == target:
            ans[0] = mid - i
            i += 1
        i = 1
        while mid + i <= len(nums) - 1 and nums[mid + i] == target:
            ans[1] = mid + i
            i+=1
        return ans
        
# @lc code=end

