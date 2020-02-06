import java.util.Arrays;
import java.util.Scanner;


public class Zathras {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int cases = sc.nextInt();
        int[][] data = new int[cases][5];
        long[] years = new long[cases];
        for(int i = 0; i < cases; i++){
            for (int k = 0; k < 5; k++) {
                if(k == 4){
                    years[i] = sc.nextLong();
                    break;
                }
                data[i][k] = sc.nextInt();
            }
        }

        int[] results = new int[2];

        for(int i = 0; i < cases; i++){
            int Acheck = data[i][0], Bcheck = data[i][0];
            for(int k = 0; k < years[i]; k++) {
                results = calc(data[i]);
                data[i][0] = results[0];
                data[i][1] = results[1];
                if (results[0] == Acheck && results[1] == Bcheck) break;
            }

            System.out.println("Case #" + (i+1) + ": " + data[i][0] + ' ' + data[i][1]);
//                Acheck = results[0];
//                Bcheck = results[1];
//            }
        }
    }

    public static int[] calc(int[] data){
        int A = data[0], B = data[1], alpha = data[2], beta = data[3], gamma = data[4];

        int offspring = (int) ((A < B ? A : B) * 0.02);

        int babyA = offspring * alpha / 100, babyB = offspring * beta / 100;
        babyA += (offspring - babyA - babyB) / 2;
        babyB = offspring - babyA;

        A = A + babyA - (int) (A * 0.01);
        B = B + babyB - (int) (B * 0.01);

        int[] result = new int[2];
        result[0] = A;
        result[1] = B;
        return result;
    }

}
