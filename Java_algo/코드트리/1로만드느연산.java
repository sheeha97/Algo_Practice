import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        int[] dp = new int[n+1];
        dp[n] = 0;

        for (int i = n-1; i >= 1; i--) {
            int[] dp_val = {n+1, n+1, dp[i+1] + 1};
            if (i * 3 <= n) {
                dp_val[0] = dp[i * 3] + 1;
            }

            if (i * 2 <= n) {
                dp_val[1] = dp[i * 2] + 1;
            }
            int min_val = n + 1;
            for (int j = 0; j < 3; j++) {
                if (min_val > dp_val[j]) {
                    min_val = dp_val[j];
                }
            }

            dp[i] = min_val;
            // System.out.println("At i " + String.valueOf(i) + " the value of dp is " + String.valueOf(dp[i]));

        }
        System.out.println(dp[1]);


    }
}