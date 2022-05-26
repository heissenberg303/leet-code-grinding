// Input: candidates = [2,3,5], target = 8
// Output: -> 6
// similar to coin change
// the way of dp[i] is accumulate of itself and remaining
class PossibleWaysofSum {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        // dp[0] = 1;
        // dp[1] = 0,
        // dp[2] = dp[2] + dp[0] -> 1
        // dp[3] = dp[3] + dp[3-2] -> 0
        // dp[3] = dp[3] + dp[3-3] -> 1
        // dp[4] = dp[4] + dp[4-2] -> 1
        // dp[4] = dp[4] + dp[4-3] -> 1
        // dp[5] = dp[5] + dp[5-2] -> 1
        // dp[5] = dp[5] + dp[5-3] -> 2
        // dp[5] = dp[5] + dp[0] -> 3
        // dp[6] = dp[6] + dp[6-2] -> 1
        // dp[6] = dp[6] + dp[6-3] -> 2
        // dp[6] = dp[6] + dp[6-5] -> 2
        // dp[7] = dp[7] + dp[7-2] -> 3
        // dp[7] = dp[7] + dp[7-3] -> 4
        // dp[7] = dp[7] + dp[7-5] -> 5
        // dp[8] = dp[8] + dp[8-2] -> 2
        // dp[8] = dp[8] + dp[8-3] -> 5
        // dp[8] = dp[8] + dp[8-5] -> 6

        for (int i = 1; i <= target; i++) {
            for (int c: nums) {
                if (i - c >= 0) {
                    dp[i] = dp[i] + dp[i - c];

                }
            }
        }
        return dp[target];
    }
}