// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution {
    public int minDeletions(String s) {

        int res = 0;
        int[] countMap = new int[26];

        for (int i=0; i<s.length(); i++)
        {
            countMap[s.charAt(i)-'a'] += 1;
        }

        Arrays.sort(countMap);

        for (int i=countMap.length - 2; i >= 0; i--)
        {
            int l = countMap[i];
            if (l==0){
                continue;
            }
            int r = countMap[i+1];
            int delta = l - r;

            if (delta >= 0){
                int cut = Math.min(l, delta + 1);
                countMap[i] -= cut;
                res += cut;
            } 
            
        }

        return res;
        
    }
}