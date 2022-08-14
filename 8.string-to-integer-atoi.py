#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
import re
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        myInt = []
        for i in range(len(s)):
            if i == 0 and s[i] == '-':myInt.append('-')
            elif re.search(r'\d',s[i]): myInt.append(s[i])
            else:break
        if len(myInt) == 0:return 0
        if s[0] in ['-','+'] and len(s) == 1: return 0
        integer = int(''.join(myInt))
        integer = pow(2,31) - 1 if integer > pow(2,31) - 1 else integer
        integer = pow(-2,31) if integer < pow(-2,31) else integer
        return integer
# @lc code=end

