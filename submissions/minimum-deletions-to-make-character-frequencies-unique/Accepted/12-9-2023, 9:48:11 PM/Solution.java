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

        List<Integer> frequencies = countMap.values().stream().collect(Collectors.toList());
        Collections.sort(frequencies);

        for (int i=frequencies.size() - 2; i >= 0; i--)
        {
            int l = frequencies.get(i);
            int r = frequencies.get(i+1);
            int delta = l - r;

            if (delta >= 0){
                int cut = Math.min(l, delta + 1);
                frequencies.set(i, l-cut);
                res += cut;
            } 
            
        }

        return res;
        
    }
}