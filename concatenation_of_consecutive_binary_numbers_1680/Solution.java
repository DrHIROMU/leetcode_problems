package concatenation_of_consecutive_binary_numbers_1680;

import java.math.BigDecimal;
import java.math.BigInteger;

public class Solution {
    public static void main(String[] args){
        int n = 12;
        concatenatedBinary(n);
    }

    public static int concatenatedBinary(int n) {
        String binStr = "";
        int result = 0;
        for(int i=1; i<=n; i++){
            String numBinStr = Integer.toBinaryString(i);
            binStr = binStr + numBinStr;
        }
        BigInteger decResult = new BigInteger(binStr, 2);
        BigInteger modNum = BigInteger.valueOf((long)Math.pow(10,9)+7);
        result = (decResult.mod(modNum).intValue());

        System.out.println(result);
        return result;
    }
}