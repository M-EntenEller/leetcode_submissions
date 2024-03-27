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
       
        for (Character c: word.toCharArray())
        {
            countMap.put(c, countMap.get(c) - 1);

            if (countMap.get(c)==0){
                countMap.remove(c);
            }

            if (countMap.values().stream().collect(Collectors.toSet()).size() == 1){
                return true;
            }
            
            if (countMap.get(c) == null){
                countMap.put(c, 0);
            }
            countMap.put(c, countMap.get(c) + 1);
        }

        return false;

    }
}