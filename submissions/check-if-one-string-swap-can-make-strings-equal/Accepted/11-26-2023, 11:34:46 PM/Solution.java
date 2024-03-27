// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution {
    public boolean areAlmostEqual(String s1, String s2) {

        int miss = 0; 
        char t1 = 0;
        char t2 = 0;

        for (int i=0; i<s1.length(); i++)
        {
            if (! (s1.charAt(i) == s2.charAt(i)))
            {
                miss++;

                if (miss < 2)
                {
                    t1 = s1.charAt(i);
                    t2 = s2.charAt(i);
                } 
                else if (miss == 2)
                {
                    if (! (t1 == s2.charAt(i) && t2 == s1.charAt(i)))
                    {
                        return false;
                    }
                } 
                else
                {
                    return false;
                }
            }
        }

        return miss != 1;
        
    }
}