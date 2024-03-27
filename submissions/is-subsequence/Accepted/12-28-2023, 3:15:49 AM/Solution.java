// https://leetcode.com/problems/is-subsequence

class Solution {
    public boolean isSubsequence(String s, String t) {

        int i=0, j=0;
        int count = 0;

        while (i<s.length() && j<t.length())
        {
            if (s.charAt(i) != t.charAt(j)){
                j++;
            } else{
                count++;
                i++;
                j++;
            }
        }

        return count == s.length();
        
    }
}