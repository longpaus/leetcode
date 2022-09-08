package javaSol;

import java.util.ArrayList;
import java.util.List;

public class kidsWithCandies {
    public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean>ans=new ArrayList()<Boolean>();
        int highestVal = 0;
        for(int num:candies){
            if(highestVal < num){
                highestVal = num;
            }
        }
        for(int num: candies){
            if(num + extraCandies >= highestVal){
                ans.add(true);
            }else{
                ans.add(false);
            }
        }
        return ans;
    }

}
