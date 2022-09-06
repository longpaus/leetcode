#!/usr/bin/env python3
class Solution:
    def binary_search(self,arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                i = mid
                while i >= 0 and arr[i] == x:
                    i -= 1
                return i + 1
        return -1

    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        m = {}
        for i in range(len(nums)):
            m[i] = nums[i]
        nums.sort()
        ans = []
        for key in m:
            ans.append(self.binary_search(nums,m[key]))
        return ans


        