// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution {
    public int minOperations(String s) {
        
        int c1 = 0;
        int c2 = 0;
        int t = 0;

        for (int i=0; i<s.length(); i++)
        {
            t = i % 2;

            if (s.charAt(i) - '0' != t)
            {
                c1++;
            }

            if (s.charAt(i) - '0' == t)
            {
                c2++;
            }
        }

        return Math.min(c1,c2);
    }
}