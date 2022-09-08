/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 */

// // @lc code=start
// /**
//  * Definition for singly-linked list.
//  * public class ListNode {
//  *     int val;
//  *     ListNode next;
//  *     ListNode() {}
//  *     ListNode(int val) { this.val = val; }
//  *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
//  * }
//  */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
            ListNode headSum = new ListNode(0);
            ListNode curr = headSum;
            int carry = 0;
            int number = 0;
            while(l1 != null || l2 != null){
                int l1Number = (l1 == null) ? 0 : l1.val;
                int l2Number = (l2 == null) ? 0 : l2.val;
                if((l1 != null && l1.next != null) || (l2 != null && l2.next != null) ){
                    number= (l1Number + l2Number + carry)%10;
                    curr.next = new ListNode(number);
                    curr = curr.next;
                    carry = (l1Number + l2Number + carry)/10;
                    
                   
                }else{
                    number= (l1Number + l2Number + carry)%10;
                    curr.next = new ListNode(number);
                    curr = curr.next;
                    carry = (l1Number + l2Number + carry)/10;
                    if(carry != 0){
                        curr.next = new ListNode(carry);                   
                    }
                }
                l1 = (l1 != null) ? l1.next : null;
                l2 = (l2 != null) ? l2.next : null;
            }
          return headSum.next;
        }
    }
}

// @lc code=end
