import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int input = Integer.parseInt(myObj.nextLine());
        long[] ret = new long[input+1];

        if (input == 1) {
            System.out.println(1);
        } else if (input == 2) {
            System.out.println(2);
        } else {
            ret[0] = 0;
            ret[1] = 1;
            ret[2] = 1;
            for (int i = 3; i < input + 1; i++) {
                ret[i] = ret[i - 1]  + ret[i - 2];
                // System.out.println(ret[i]);
            }
            System.out.println(ret[input]);
        }

    }
}