/*
 * @lc app=leetcode id=1 lang=typescript
 *
 * [1] Two Sum
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
    let map = {}
    for(let i = 0; i < nums.length; i++){
        if(target - nums[i] in map){
            return[map[target - nums[i]].index,i]
        }
        map[nums[i]] = {index:i}
    }
    return []
};
// @lc code=end

