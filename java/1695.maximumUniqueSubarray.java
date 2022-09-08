package java;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int maximumUniqueSubarray(int[] nums) {
        Set<Integer> numSet = new HashSet<Integer>();
        int left = 0;
        int sum = 0;
        int highest = 0;
        for(int right = 0;right < nums.length; right++){
            if(!numSet.contains(nums[right])){
                numSet.add(nums[right]);
                sum += nums[right];
            }
            else{
                while(nums[left] != nums[right]){
                    numSet.remove(nums[left]);
                    sum -= nums[left];
                    left++;
                }
                left++;
            }
            if(sum > highest){
                highest = sum;
            }
        }
        return highest;
    }
}
