package medium.sort_characters_by_frequency_451;

import java.util.*;

public class Solution {
    public static void main(String[] args){
        Solution solution = new Solution();
        String s = "Aabb";
        System.out.println(solution.frequencySort(s));
    }

    public String frequencySort(String s) {
        Map<Character, String> appearStrMap = new HashMap<>();
        List<String> appearFreqCharList = new LinkedList<>();
        char[] chars = s.toCharArray();
        StringBuffer stringBuffer = new StringBuffer();

        for(char c : chars){
            if(!appearStrMap.containsKey(c)){
                appearStrMap.put(c, "");
            }
            String appearString = appearStrMap.get(c)+c;
            appearStrMap.put(c, appearString);
        }

        while(appearStrMap.keySet().size()>0){
            Character mostFreqAppearChar=null;
            int maxLen = 0;
            for(Character key : appearStrMap.keySet()){
                int strLen = appearStrMap.get(key).length();
                if(strLen>maxLen){
                    maxLen = strLen;
                    mostFreqAppearChar = key;
                }
            }
            stringBuffer.append(appearStrMap.get(mostFreqAppearChar));
            appearStrMap.remove(mostFreqAppearChar);
        }


        return stringBuffer.toString();
    }
}
