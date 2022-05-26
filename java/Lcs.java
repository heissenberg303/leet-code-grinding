class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // text1 = "abcde" , text2 = "ace" -> 3
        // text1 = "acacac", text2 = "ac" -> 2
        //  default is 0
        int[][] dpGrid = new int[text1.length() + 1][text2.length() + 1];

        for (int col = text2.length() - 1 ; col >= 0; col--) {
            for (int row = text1.length() - 1; row >= 0; row--) {
                if (text1.charAt(row) == text2.charAt(col)) {
                    dpGrid[row][col] = 1 + (dpGrid[row + 1][col + 1]); // 1 + dpGrid of index before
                }
                else {
                    dpGrid[row][col] = Math.max(dpGrid[row + 1][col], dpGrid[row][col + 1]);
                }
            }
        }
        return dpGrid[0][0];

    }
}