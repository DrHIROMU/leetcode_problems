package medium.longest_palindromic_substring_5;

import java.util.LinkedList;
import java.util.List;

public class Solution {
    public static void main(String[] args){
        Solution solution = new Solution();
//        System.out.println(solution.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"));
        System.out.println(solution.longestPalindrome("a"));

    }

    public String longestPalindrome(String s) {
        char[] charArr = s.toCharArray();

        int leftCharIndex, rightCharIndex;
        String palindromeStr = "";
        int palindromeLen = 0;

        //odd case
        for(int i=0; i<s.length(); i++){
            leftCharIndex = i;
            rightCharIndex = i;

            while(leftCharIndex>=0
                    && rightCharIndex < s.length()
                    && charArr[leftCharIndex] == charArr[rightCharIndex]){
                if(rightCharIndex - leftCharIndex + 1 > palindromeLen){
                    palindromeStr = s.substring(leftCharIndex, rightCharIndex+1);
                    palindromeLen = rightCharIndex - leftCharIndex + 1;
                }
                leftCharIndex -= 1;
                rightCharIndex +=1;
            }
        }

        //even case
        for(int i=0; i<s.length(); i++){
            leftCharIndex = i;
            rightCharIndex = i+1;
            while(leftCharIndex>=0
                    && rightCharIndex < s.length()
                    && charArr[leftCharIndex] == charArr[rightCharIndex]){
                if(rightCharIndex - leftCharIndex + 1 > palindromeLen){
                    palindromeStr = s.substring(leftCharIndex, rightCharIndex+1);
                    palindromeLen = rightCharIndex - leftCharIndex + 1;
                }
                leftCharIndex -= 1;
                rightCharIndex +=1;
            }
        }

        return palindromeStr;
    }
}
