// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique

class Solution {
    public int minDeletions(String s) {

        int res = 0;
        Map<Character,Integer> countMap = new HashMap<>();

        for (int i=0; i<s.length(); i++)
        {
            Integer tmp = countMap.get(s.charAt(i));

            if (tmp == null){
                countMap.put(s.charAt(i), 1);
            } else {
                countMap.put(s.charAt(i), tmp + 1);
            }
        } 

        int[] frequencies = new int[countMap.size()];
        int idx = 0;

        for (Integer x: countMap.values())
        {
            frequencies[idx++] = (int) x;
        }

        Arrays.sort(frequencies);

        for (int i=frequencies.length - 2; i >= 0; i--)
        {
            int delta = frequencies[i] - frequencies[i+1];

            if (delta >= 0){
                int cut = Math.min(frequencies[i], delta + 1);
                frequencies[i] -= cut;
                res += cut;
            } 
            
        }

        return res;
        
    }
}