// https://leetcode.com/problems/lexicographically-smallest-palindrome

class Solution {
    public String makeSmallestPalindrome(String s) {
        
        char[] sA = s.toCharArray(); 
        int l = 0;
        int u = s.length()-1;

        while (l < u)
        {
            sA[l] = sA[u] = (char) Math.min(sA[l], sA[u]);
            l++;
            u--;
        }

        return new String(sA);

    }
}