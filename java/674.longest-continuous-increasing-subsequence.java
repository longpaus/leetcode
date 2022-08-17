package java;
/*
 * @lc app=leetcode id=674 lang=java
 *
 * [674] Longest Continuous Increasing Subsequence
 */

// @lc code=start
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int anchor = 0;
        int longest = 1;
        for(int i = 0; i + 1 < nums.length; i++){
             if(nums[i] < nums[i + 1] && longest < (i + 1) - anchor + 1)
                longest = (i + 1) - anchor + 1;
            else if (nums[i] >= nums[i + 1])  
                anchor = i + 1;
        }
        return longest;
    }
}
// @lc code=end

