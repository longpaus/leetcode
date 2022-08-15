/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    if(x < 0){
        return false
    }
    let numStr: string = x.toString()
    if(numStr.length % 2 === 0){
       for(let i = 0; i < numStr.length/2; i++){
           if(numStr[i] != numStr[numStr.length - 1 - i]){
                return false
            }
       }
    }else{
        for(let i = 0; i < (numStr.length - 1)/2; i++){
            if(numStr[i] != numStr[numStr.length - 1 - i]){
                return false
            }
        }
    }
    return true
};
// @lc code=end

