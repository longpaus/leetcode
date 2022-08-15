/*
 * @lc app=leetcode id=26 lang=java
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 1;
        for(int i = 0; i + 1 < nums.length; i++){
            if(nums[i] != nums[i + 1]){
                nums[index] = nums[i + 1];
                index++;
            }
        }
        return index;
    }
}
// @lc code=end

