#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
from curses.ascii import isdigit
from turtle import pos


class Solution:
    def myAtoi(self, s: str) -> int:
        num = "0"
        positive = True
        for i in range(len(s)):
            if s[i] == '-' and s[i + 1].isdigit():
                positive = False
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    num+=s[j]
                    j+=1 
                break
        return int(num) if positive else -1*int(num)

        
# @lc code=end

