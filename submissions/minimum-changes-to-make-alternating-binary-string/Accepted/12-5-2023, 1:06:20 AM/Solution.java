// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution {
    public int minOperations(String s) {
        
        int c1 = 0;

        for (int i=0; i<s.length(); i++)
        {
            if (s.charAt(i) - '0' != (i % 2))
            {
                c1++;
            }
        }

        return Math.min(c1, s.length()-c1);
    }
}