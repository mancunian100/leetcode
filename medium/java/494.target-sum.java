/*
 * @lc app=leetcode id=494 lang=java
 *
 * [494] Target Sum
 */
class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        if (sum < S || (sum + S) % 2 != 0) {
            return 0;
        }
        int target = (sum + S) / 2;
        int dp[] = new int[target + 1];
        dp[0] = 1;
        for (int n : nums) {
            for (int j = target; j >= n; j--) {
                dp[j] = dp[j] + dp[j - n];
            }
        }
        return dp[target];
    }
}

