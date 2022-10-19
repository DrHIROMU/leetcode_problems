package easy.two_sum_1;

public class Solution {
    public static void main(String[] args){
        int[] nums = {2,7,11,15};
        int target = 9;
        twoSum(nums, target);
    }

    public static int[] twoSum(int[] nums, int target) {
        int[] indices = new int[2];
        for(int i=0; i<nums.length; i++){
            int num1 = nums[i];

            for(int j=i+1; j<nums.length; j++){
                int num2 = nums[j];
                if(num1 + num2 == target){
                    indices[0] = i;
                    indices[1] = j;
                    break;
                }
            }
        }
        return indices;
    }
}
