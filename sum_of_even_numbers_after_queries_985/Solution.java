package sum_of_even_numbers_after_queries_985;

public class Solution {
    public static void main(String[] args){
        int[] nums = {1,2,3,4};
        int[][] queries = {{1,0},{-3,1},{-4,0},{2,3}};

       sumEvenAfterQueries(nums, queries);
    }

    public static int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int[] answers = new int[queries.length];
        int queryRound = 0;

        int sumOfQuery = 0;
        boolean[] numsBeSumUp = new boolean[nums.length];

        for(int i=0; i<nums.length; i++){
            int num = nums[i];
            if(num % 2 == 0){
                numsBeSumUp[i] = true;
                sumOfQuery += num;
            }
        }

        for(int[] query : queries){
            int value = query[0];
            int index = query[1];

            if((nums[index] + value) % 2 == 0){
                if(numsBeSumUp[index]){
                    sumOfQuery += value;
                }else{
                    sumOfQuery += nums[index] + value;
                    numsBeSumUp[index] = true;
                }
            }else{
                if(numsBeSumUp[index]){
                    sumOfQuery -= nums[index];
                    numsBeSumUp[index] = false;
                }
            }
            nums[index] = nums[index] + value;

            answers[queryRound++] = sumOfQuery;
        }

        return answers;
    }
}
