#!/usr/bin/env python3
from collections import defaultdict




class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        m = defaultdict(lambda:0)
        for num in arr:
            m[num] += 1
        m = {k: v for k, v in sorted(m.items(), key=lambda item: item[1])}
        count = len(m)
        for key in m:
            while m[key] > 0 and k > 0:
                m[key] -= 1
                k -= 1
            if m[key] == 0:
                count -= 1
            if k == 0:
                break
        return count
