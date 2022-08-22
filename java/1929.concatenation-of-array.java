/*
 * @lc app=leetcode id=1929 lang=java
 *
 * [1929] Concatenation of Array
 */

// @lc code=start
class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[2*nums.length];
        for(int i = 0; i < nums.length; i++){
            ans[i] = nums[i];
        }
        int k = nums.length;
        for(int i = 0; i < nums.length; i++){
            ans[k++] = nums[i];
        }
        return ans;
    }
}
// @lc code=end

