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
        for(int[] query : queries){
            int sumOfQuery = 0;
            int value = query[0];
            int index = query[1];
            nums[index] = nums[index] + value;
            for(int num : nums){
                if(num % 2 == 0){
                    sumOfQuery += num;
                }
            }
            answers[queryRound++] = sumOfQuery;
        }

        return answers;
    }
}
