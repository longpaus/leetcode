#!/usr/bin/env python3

from collections import defaultdict


class Solution:
    def largestPalindromic(self, num: str) -> str:
        m = defaultdict(lambda: 0)
        for l in num:
            m[l] += 1
        m = dict(sorted(m.items(), reverse=True))
        odd = ""
        ans = ""
        for key in m:
            if m[key] % 2 == 0:
                for i in range(m[key]//2):
                    ans += key
            elif m[key] % 2 != 0:
                if len(odd) == 0:
                    odd = key
                for i in range((m[key] - 1)//2):
                    ans += key
        j = 0
        while j < len(ans) and ans[j] == '0':
            j += 1
        ans = ans[j:]
        return ans + odd + ans[::-1] if len(ans + odd + ans[::-1]) != 0 else '0'


