from itertools import izip

class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []
        for i,j in zip(nums[:n],nums[n:]):
            ans.append(i)
            ans.append(j)
        return ans
