// https://leetcode.com/problems/maximum-number-of-pairs-in-array

class Solution {
    public int[] numberOfPairs(int[] nums) {
        
        int pairs = 0; 
        Map<Integer, Integer> countMap = new HashMap<>();

        for (Integer num: nums){

            if (countMap.get(num) != null){
                countMap.put(num, countMap.get(num) + 1);
            } else{
                countMap.put(num, 1);
            }

        }
        
        for(var e: countMap.entrySet()){
            pairs += e.getValue() / 2;
        }

        return new int[]{pairs, nums.length - pairs*2};

    }
}