package concatenation_of_consecutive_binary_numbers_1680;

import java.math.BigDecimal;
import java.math.BigInteger;

public class Solution {
    public static void main(String[] args){
        int n = 12;
        concatenatedBinary(n);
    }

    public static int concatenatedBinary(int n) {
        /*
        1 = 1
        2 = 110
        3 = 11011
        4 = 11011100
         */
        Long result = 1L;
        Long len = 4L;
        for (int i = 2; i <= n; i++) {
            if(len == i) len *= 2;
            result = (result*len+i) % 1000000007L;
        }
        return result.intValue();
    }
}