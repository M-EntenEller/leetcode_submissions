// https://leetcode.com/problems/longest-palindrome

class Solution {
    public int longestPalindrome(String s) {

        Map<Integer, Integer> countMap = new HashMap<>();
        boolean uneven = false;
        int longest = 0;
        int rest = 0; 

        s.chars().forEach((c)->{
            if (countMap.get(c) == null)
            {
                countMap.put(c, 1);
            }
            else
            {
                countMap.put(c, countMap.get(c) + 1);
            }
        });

        for (var c : countMap.values())
        {
            if (c == 0)
            {
                continue;
            }

            if ((rest = c % 2) == 1)
            {
                uneven = true;
            }

            longest += c-rest;
        }

        return longest + (uneven ? 1 : 0);
    }
}