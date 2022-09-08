#!/usr/bin/env python3
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        numSet = set()
        left,highest,s = 0,0,0
        for right in range(len(nums)):
            if nums[right] not in numSet:
                numSet.add(nums[right])
                s += nums[right]
            else:
                while nums[left] != nums[right]:
                    numSet.remove(nums[left])
                    s -= s[left]
                    left += 1
                left += 1
            if s > highest:
                highest = s
        return highest

test = Solution()
print(test.maximumUniqueSubarray([1,1,1,1]))
