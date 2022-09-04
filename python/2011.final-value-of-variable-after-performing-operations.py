#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        val = 0
        for oper in operations:
            if oper[0] == '-' or oper[-1] == '-':
                val -= 1
            elif oper[0] == '+' or oper[-1] == '+':
                val += 1
        return val
        
# @lc code=end

