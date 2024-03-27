// https://leetcode.com/problems/split-a-string-in-balanced-strings

class Solution {
    public int balancedStringSplit(String s) {
        
        int count=0;
        int bal = 0;

        for (int i=0; i<s.length(); i++)
        {
            bal += s.charAt(i) == 'R' ? 1 : -1;

            if (bal==0){
                count++;
            }
        }

        return count;

    }
}