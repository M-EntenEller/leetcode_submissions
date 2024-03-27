// https://leetcode.com/problems/longest-palindrome

class Solution {
    public int longestPalindrome(String s) {

        char[] countMap = new char[128];
        boolean uneven = false;
        int longest = 0;
        int rest = 0;

        s.chars().forEach(c->countMap[c]++);

        for(char c: countMap)
        {
            if (c == 0)
            {
                continue;
            }

            if ((rest = c % 2) == 1)
            {
                uneven =true;
            }

            longest += c-rest;

        }
        
        return longest + (uneven ? 1 : 0);
    }
}