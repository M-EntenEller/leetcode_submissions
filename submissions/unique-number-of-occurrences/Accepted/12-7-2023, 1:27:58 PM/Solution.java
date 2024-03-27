// https://leetcode.com/problems/unique-number-of-occurrences

class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        
        Map<Integer, Integer> countMap = new HashMap<>();
        Set<Integer> countSeen = new HashSet<>();
        Integer tmp;

        for (int i=0; i<arr.length; i++)
        {
            tmp = countMap.get(arr[i]); 

            if (tmp == null){
                countMap.put(arr[i], 1); 
            } else{
                countMap.put(arr[i], tmp + 1);
            }
        }

        for (Integer count: countMap.values())
        {
            if (countSeen.contains(count)){
                return false;
            }
            countSeen.add(count);
        }

        return true;
    }
}