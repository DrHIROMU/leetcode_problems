package easy.palindrome_number_9;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    public static void main(String[] args){
        isPalindrome(313);
    }

    public static boolean isPalindrome(int x) {
        List<Integer> numOfDigits = new ArrayList<>();
        Integer palindromeNum = 0;
        Integer inputNum = x;
        while (x > 0) {
            int numOfDigit = x % 10;
            x = x / 10;
            numOfDigits.add(numOfDigit);
        }
        for(Integer num : numOfDigits){
            palindromeNum = palindromeNum*10 + num;
        }
        if(!inputNum.equals(palindromeNum)){
           return false;
        }

        return true;
    }
}
