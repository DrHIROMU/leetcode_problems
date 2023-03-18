package medium.lexicographically_smallest_equivalent_string_1061;

import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "bcfeaabddgcdaefcbfadggfagfgfedeefbebdbeefbecggcgge";
        String s2 = "feegaacabcfadggfcaabcbadbbecbfdcabgeaegfcagdfggdgg";
        String baseStr = "mytnpodxbwxcxcplapgrqjzkfrkizffkbquwqbkxmpqjmxykvb";
//        "mytnpoaxawxaxaplaparqjzkarkizaakaquwqakxmpqjmxykva"
        String result = solution.smallestEquivalentString(s1, s2, baseStr);
        System.out.println(result);
    }

    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        String result = "";
        Map<Character, Character> charMap = new HashMap<>();
        Map<Character, Set<Character>> charGroupMap = new HashMap<>();

        Character smallestLetter;
        for(int i=0; i<s1.length(); i++){
            Character c1 = s1.charAt(i);
            Character c2 = s2.charAt(i);
            Set<Character> charGroup = null;

            if(charGroupMap.containsKey(c1)){
                charGroup = charGroupMap.get(c1);
            }
            if(charGroupMap.containsKey(c2)){
                if(charGroup == null){
                    charGroup = charGroupMap.get(c2);
                }else{
                    charGroup.addAll(charGroupMap.get(c2));
                }
            }

            if(charGroup == null){
                charGroup = new HashSet<>();
                charGroup.add(c1);
                charGroup.add(c2);
                charGroupMap.put(c1, charGroup);
                charGroupMap.put(c2, charGroup);

                smallestLetter = c1;
                if(c2 < smallestLetter){
                    smallestLetter = c2;
                }
                charMap.put(c1, smallestLetter);
                charMap.put(c2, smallestLetter);
            }else{
                charGroup.add(c1);
                charGroup.add(c2);
                smallestLetter = c1;
                for(Character c : charGroup){
                    charGroupMap.put(c, charGroup);

                    if(c < smallestLetter){
                        smallestLetter = c;
                    }
                }

                for(Character c : charGroup){
                    charMap.put(c, smallestLetter);
                }
            }
        }

        for(Character c : baseStr.toCharArray()){
            smallestLetter = charMap.get(c);
            if(smallestLetter == null){
                result = result + c;
            }else{
                result = result + smallestLetter;
            }
        }

        System.out.println(charGroupMap);
        System.out.println(charMap);

        return result;
    }
}
