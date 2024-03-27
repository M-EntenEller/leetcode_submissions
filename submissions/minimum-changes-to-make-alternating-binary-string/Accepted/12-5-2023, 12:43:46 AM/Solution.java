// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string

class Solution {
    public int minOperations(String s) {
        
        int c1 = 0;
        int c2 = 0;

        for (int i=0; i<s.length(); i++)
        {
            if (s.charAt(i) == (i % 2 == 0 ? '0' : '1'))
            {
                c1++;
            }

            if (s.charAt(i) == (i % 2 != 0 ? '0' : '1'))
            {
                c2++;
            }
        }

        return Math.min(c1,c2);
    }
}