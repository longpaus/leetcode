package java;
/*
 * @lc app=leetcode id=27 lang=java
 *
 * [27] Remove Element
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int j = 0;
        for(int num : nums){
            if(num != val){
                nums[j] = num;
                j++;
            }
        }
        return j;
    }
}
// @lc code=end

