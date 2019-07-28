/*
 * @lc app=leetcode id=416 lang=java
 *
 * [416] Partition Equal Subset Sum
 */
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        if (sum % 2 != 0) {
            return false;
        }
        int s = sum / 2;
        boolean dp[] = new boolean[s + 1];
        dp[0] = true;
        for (int n : nums) {
            for (int j = s; j > 0; j--) {
                if (j >= n) {
                    dp[j] = (dp[j] || dp[j - n]);
                }
            }
        }
        return dp[s];
    }
}

