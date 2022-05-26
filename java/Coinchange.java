import java.util.Arrays;
// similar to possibles ways but involve greedy algorithm
// always choose minimum
class Coinchange {
    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int amount = 11;
        System.out.println(coinChange(coins, amount));
    }
    public static int coinChange(int[] coins, int amount) {

        int[] dp = new int[amount+1];
        // Arrays.fill(dp, amount + 1);
        fillArray(dp, amount+1);

        dp[0] = 0;
            for (int i = 1; i < amount + 1; i++) {
                for (int c: coins) {
                   if (i - c >= 0) {
                       dp[i] = Math.min(dp[i], 1 + dp[i-c]);
                   }
                }

            }
            if (dp[amount] != amount + 1) {
                return dp[amount];
            }
            else {
                return -1;
            }
    }
    public static int[] fillArray(int[] arr, int number) {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = number;
        }
        return arr;
    }

}