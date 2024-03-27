// https://leetcode.com/problems/remove-letter-to-equalize-frequency

class Solution {
    public boolean equalFrequency(String word) {

        Map<Character, Integer> countMap = new HashMap<>();

        for (var c: word.toCharArray())
        {
            if (countMap.get(c) == null){
                countMap.put(c, 0);
            }
            countMap.put(c, countMap.get(c) + 1);
        }
       
        for (Character c: countMap.keySet())
        {
            countMap.put(c, countMap.get(c) - 1);
            if (countMap.values().stream().filter(e->e>0).distinct().count() == 1){
                return true;
            }
            countMap.put(c, countMap.get(c) + 1);
        }

        return false;

    }
}