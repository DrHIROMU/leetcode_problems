package easy.roman_to_integer_13;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args){
        Solution solution = new Solution();
        int result = solution.romanToInt("MCMXCIV");
        System.out.println(result);
    }

    public int romanToInt(String s) {
        int result = 0;
        Map<Character, Integer> romanNumMap = setRomanNumMap();

        boolean passChar = false;

        for(int i=0; i<s.toCharArray().length; i++){
            Character c = s.toCharArray()[i];
            Character nextRomanNum;
            int num = romanNumMap.get(c);

            if(passChar){
                passChar = false;
                continue;
            }

            if(i != s.toCharArray().length-1){
                if(c.equals('C')){
                    nextRomanNum = s.toCharArray()[i+1];
                    if(nextRomanNum.equals('D')){
                        num = 400;
                        passChar = true;
                    }else if(nextRomanNum.equals('M')){
                        num = 900;
                        passChar = true;
                    }
                }else if(c.equals('X')){
                    nextRomanNum = s.toCharArray()[i+1];
                    if(nextRomanNum.equals('L')){
                        num = 40;
                        passChar = true;
                    }else if(nextRomanNum.equals('C')){
                        num = 90;
                        passChar = true;
                    }
                }else if(c.equals('I')){
                    nextRomanNum = s.toCharArray()[i+1];
                    if(nextRomanNum.equals('V')){
                        num = 4;
                        passChar = true;
                    }else if(nextRomanNum.equals('X')){
                        num = 9;
                        passChar = true;
                    }
                }
            }
            result += num;
        }
        return result;
    }

    private Map<Character, Integer> setRomanNumMap(){
        Map<Character, Integer> romanNumMap = new HashMap<>();
        romanNumMap.put('I', 1);
        romanNumMap.put('V', 5);
        romanNumMap.put('X', 10);
        romanNumMap.put('L', 50);
        romanNumMap.put('C', 100);
        romanNumMap.put('D', 500);
        romanNumMap.put('M', 1000);
        return romanNumMap;
    }
}
