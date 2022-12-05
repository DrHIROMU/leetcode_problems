package medium.minimum_average_difference_2256;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args){
        Solution solution = new Solution();
        int[] nums = {1,2,3,4,5};
        int result = solution.minimumAverageDifference(nums);
        System.out.println(result);
    }

    public int minimumAverageDifference(int[] nums) {
        int result=-1;
        int diffOfAvg=0;
        int minAvg=-1;

        long prevSumA=0;
        long prevSumB=0;

        if(nums.length == 0){
            return 0;
        }
        if(nums.length == 1){
            return 0;
        }

        for(int i=0; i<nums.length; i++){
            long sumA=0, sumB=0;
            long avgA=0, avgB=0;

            if(i==0){
                sumA = nums[0];
                prevSumA = nums[0];
            }else{
                sumA = nums[i]+prevSumA;
                prevSumA = sumA;
            }

            if(i==0){
                for(int j=i+1; j< nums.length; j++){
                    sumB += nums[j];
                }
                prevSumB=sumB;
            }else{
                sumB = prevSumB-nums[i];
                prevSumB = sumB;
            }

            avgA = sumA/(i+1);
            avgB = sumB!=0? sumB/(nums.length-i-1) : 0;

            diffOfAvg = Math.abs((int)(avgA - avgB));
            if(diffOfAvg==0) return i;

            if(result == -1){
                result = i;
                minAvg = diffOfAvg;
            }else if(diffOfAvg < minAvg){
                result = i;
                minAvg = diffOfAvg;
            }
        }

        return result;
    }
}
