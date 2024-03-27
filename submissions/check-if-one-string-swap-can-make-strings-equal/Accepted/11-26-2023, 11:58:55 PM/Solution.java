// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal

class Solution {
    public boolean areAlmostEqual(String s1, String s2) {

        int miss = 0; 
        int[] indexArr = new int[2];

        for (int i=0; i<s1.length(); i++)
        {
            if (! (s1.charAt(i) == s2.charAt(i)))
            {
                miss++;

                if (miss > 2)
                {
                    return false;
                }
                
                indexArr[miss-1] = i;
                
            }
        }

        switch (miss)
        {
            case 0:
                return true;
            case 1:
                return false;
        }

        return s1.charAt(indexArr[0]) ==  s2.charAt(indexArr[1]) 
                && s2.charAt(indexArr[0]) == s1.charAt(indexArr[1]);
        
    }
}