package cinema_seat_allocation1386;

import java.io.InputStream;
import java.util.Properties;

class Solution {
    public static void main(String[] args) {
        try{
            int[][] reserveSeats;
            Properties properties = new Properties();
            InputStream inputStream = Solution.class.getResourceAsStream("input.properties");
            properties.load(inputStream);
            String a = inputStream.toString();
//            int result = maxNumberOfFamilies(1000000000, reserveSeats);
            System.out.println("a");
        }catch (Exception ex){
            System.out.println(ex);
        }
    }

    public static int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        int numOfFourPersonSeats = 0;
        int[][] availableFourPersonSeats = new int[n][3];

        for (int i = 0; i < n; i++) {
            availableFourPersonSeats[i][0] = 1;
            availableFourPersonSeats[i][1] = 1;
            availableFourPersonSeats[i][2] = 1;
        }

        for (int i = 0; i < reservedSeats.length; i++) {
            int[] reserveSeat = reservedSeats[i];
            int row = reserveSeat[0] - 1;
            int col = reserveSeat[1] - 1;
            switch (col) {
                case 1:
                case 2:
                    availableFourPersonSeats[row][0] = 0;
                    break;
                case 3:
                case 4:
                    availableFourPersonSeats[row][0] = 0;
                    availableFourPersonSeats[row][1] = 0;
                    break;
                case 5:
                case 6:
                    availableFourPersonSeats[row][1] = 0;
                    availableFourPersonSeats[row][2] = 0;
                    break;
                case 7:
                case 8:
                    availableFourPersonSeats[row][2] = 0;
                    break;
            }
        }

        for (int i = 0; i < n; i++) {
            if (availableFourPersonSeats[i][0] == 1 || availableFourPersonSeats[i][2] == 1) {
                availableFourPersonSeats[i][1] = 0;
            }
            for (int j = 0; j < 3; j++) {
                numOfFourPersonSeats += availableFourPersonSeats[i][j];
            }
        }

        return numOfFourPersonSeats;
    }
}
