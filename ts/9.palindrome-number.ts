/*
 * @lc app=leetcode id=9 lang=typescript
 *
 * [9] Palindrome Number
 */

// @lc code=start
function isPalindrome(x: number): boolean {
    if(x < 0){
        return false;
    }
    let string = x.toString()
    let reverse = ''
    for (var i = string.length - 1; i >= 0; i--) { 
        reverse += string[i]; 
    }
    return (reverse === string) ? true : false
};
// @lc code=end

