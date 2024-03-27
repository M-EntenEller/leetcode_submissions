// https://leetcode.com/problems/longest-palindrome

class Solution {
    public int longestPalindrome(String s) {

        Map<Character, Integer> countMap = new HashMap<>();
        int oddCount = 0;
        int longest = 0;
        int rest = 0; 

        for (int i=0; i<s.length(); i++)
        {
            char c = s.charAt(i);

            if (countMap.get(c) == null)
            {
                countMap.put(c, 1);
            }
            else
            {
                countMap.put(c, countMap.get(c) + 1);
            }
            if (countMap.get(c) % 2 == 0)
            {
                oddCount--;
            }
            else
            {
                oddCount++;
            }
        }

        if (oddCount > 0){
            return s.length() - oddCount + 1; 
        }

        return s.length();

        
    }
}