// https://leetcode.com/problems/longest-string-chain

class Solution {

    public int longestStrChain(String[] words) {

        Map<String,Integer> dp = new HashMap<>();
        int res = 0;

        Arrays.sort(words, (a,b)->a.length()-b.length());
        
        for (String word:words)
        {
            int best =0;

            for (int i=0; i<word.length();i++)
            {
                best = Math.max(best,dp.getOrDefault(word.substring(0,i) + word.substring(i+1), 0) + 1);    
            }

            dp.put(word, best);
            res = Math.max(best, res);
        }

        return res;
    }
}