package medium.longest_substring_without_repeating_characters_3;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    public static void main(String[] args){
        String s = "wobgrovw";
        Solution solution = new Solution();
        System.out.println(solution.lengthOfLongestSubstring(s));
    }

    public int lengthOfLongestSubstring(String s) {
        Set<Character> charSet = new HashSet<>();
        StringBuffer maxNonRepeatSubStr = new StringBuffer();
        int currentMaxNonRepeatStrLen = 0;
        //最多字串不相同的字元數
        if(s.length() == 1) return 1;

        for(char c : s.toCharArray()){
            if(!charSet.contains(c)){
                charSet.add(c);
                maxNonRepeatSubStr = maxNonRepeatSubStr.append(c);
            }else{
                int repeatCharIndex = 0;
                for(char cInNonRepeatStr : maxNonRepeatSubStr.toString().toCharArray()){
                    if(cInNonRepeatStr == c){
                        break;
                    }
                    repeatCharIndex++;
                }

                maxNonRepeatSubStr =
                        new StringBuffer(
                                maxNonRepeatSubStr.toString().substring(repeatCharIndex+1, maxNonRepeatSubStr.length())
                        ).append(c);

                charSet.clear();
                for(char nonRepeteChar : maxNonRepeatSubStr.toString().toCharArray()){
                    charSet.add(nonRepeteChar);
                }
            }
            currentMaxNonRepeatStrLen = maxNonRepeatSubStr.length()>currentMaxNonRepeatStrLen?
                    maxNonRepeatSubStr.length() : currentMaxNonRepeatStrLen;
        }

        return currentMaxNonRepeatStrLen;
    }
}
