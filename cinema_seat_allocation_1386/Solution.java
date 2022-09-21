package cinema_seat_allocation_1386;


class Solution {
    public static void main(String[] args) {
        try {
//            InputStream input = new FileInputStream("input.properties")
//            Properties prop = new Properties();

            // load a properties file
//            prop.load(input);

//            int[][] reserveSeats= {{4,3},{1,4},{4,6},{1,7}};

            int[][] reserveSeats= 
            {{2,10},{3,7},{1,5},{1,10},{1,1},{2,5},{1,4},{3,5},{1,7},{3,1},{3,3},{3,4},{1,9},{2,1},{3,2},{1,3},{2,8},{2,2},{1,6},{2,4},{3,6},{1,8},{3,8}};
            
            
            int result = maxNumberOfFamilies(3, reserveSeats);
            System.out.println(result);
        }catch (Exception ex){
            System.out.println(ex);
        }
    }

    public static int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        int numOfFourPersonSeats = 0;
        byte[] availableFourPersonSeats = new byte[n];

        for (int i = 0; i < reservedSeats.length; i++) {
            int[] reserveSeat = reservedSeats[i];
            int row = reserveSeat[0] - 1;
            int col = reserveSeat[1] - 1;

            if(availableFourPersonSeats[row] == 0) availableFourPersonSeats[row] = 7;
            if(availableFourPersonSeats[row] == -1) continue;

            switch (col) {
                case 1:
                case 2:
                    if(availableFourPersonSeats[row] != 3 && availableFourPersonSeats[row] != 2 && availableFourPersonSeats[row] != 1){
                        availableFourPersonSeats[row] = (byte) (availableFourPersonSeats[row]-4);
                    }
                    break;
                case 3:
                case 4:
                    if(availableFourPersonSeats[row] != 3 && availableFourPersonSeats[row] != 2 && availableFourPersonSeats[row] != 1){
                        availableFourPersonSeats[row] = (byte) (availableFourPersonSeats[row]-4);
                    }
                    if(availableFourPersonSeats[row] != 4 && availableFourPersonSeats[row] != 5 && availableFourPersonSeats[row] != 1 && availableFourPersonSeats[row] != 0){
                        availableFourPersonSeats[row] = (byte) (availableFourPersonSeats[row]-2);
                    }
                    break;
                case 5:
                case 6:
                    if(availableFourPersonSeats[row] != 4 && availableFourPersonSeats[row] != 5 && availableFourPersonSeats[row] != 1){
                        availableFourPersonSeats[row] = (byte) (availableFourPersonSeats[row]-2);
                    }
                    if(availableFourPersonSeats[row] != 6 && availableFourPersonSeats[row] != 4 && availableFourPersonSeats[row] != 2 && availableFourPersonSeats[row] != 0){
                        availableFourPersonSeats[row] = (byte) (availableFourPersonSeats[row]-1);
                    }
                    break;
                case 7:
                case 8:
                    if(availableFourPersonSeats[row] != 6 && availableFourPersonSeats[row] != 4 && availableFourPersonSeats[row] != 2){
                        availableFourPersonSeats[row] = (byte) (availableFourPersonSeats[row]-1);
                    }
                    break;
            }
            if(availableFourPersonSeats[row] == 0){
                availableFourPersonSeats[row] = -1;
            }
        }

        for (int i = 0; i < n; i++) {
            if (availableFourPersonSeats[i] == 7 || availableFourPersonSeats[i]== 0) {
                numOfFourPersonSeats += 2;
            }else if(availableFourPersonSeats[i] != -1){
                numOfFourPersonSeats += 1;
            }
        }

        return numOfFourPersonSeats;
    }
}
