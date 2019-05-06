/*
 * @lc app=leetcode id=6 lang=java
 *
 * [6] ZigZag Conversion
 */
class Solution {
    public String convert(String s, int numRows) {
        if (numRows < 2 || s == null) {
            return s;
        }
        char[] arr = s.toCharArray();
        StringBuffer[] sb = new StringBuffer[numRows];
        for (int i = 0; i < numRows; i += 1) {
            sb[i] = new StringBuffer();
        }
        for (int i = 0; i < arr.length; i += 1) {
            int index = i % (2 * (numRows - 1));
            if (index < numRows) {
                sb[index].append(arr[i]);
            } else {
                index = 2 * (numRows - 1) - index;
                sb[index].append(arr[i]);
            }
        }
        StringBuffer res = new StringBuffer();
        for (int i = 0; i < numRows; i += 1) {
            res.append(sb[i]);
        }
        return String.valueOf(res);
    }
}

