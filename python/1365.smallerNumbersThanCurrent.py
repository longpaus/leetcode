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
        tmp = list(sorted(nums))
        ans = []
        for i in range(len(nums)):
            ans.append(self.binary_search(tmp,nums[i]))
        return ans

        