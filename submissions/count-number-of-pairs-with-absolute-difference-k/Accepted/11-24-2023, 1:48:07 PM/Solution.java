// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k

class Solution {

    private void putVal(Map<Integer,Integer> h, int v1){
        
        Integer current; 

        if ((current = h.get(v1)) != null){
            h.put(v1, current + 1);
        } else{
            h.put(v1, 1);   
        }

    }

    public int countKDifference(int[] nums, int k) {

        int pairs = 0;
        Map<Integer,Integer> seen = new HashMap<>(); // key -> mult
        Integer mult = 0;

        for (int num: nums){

            if ((mult = seen.get(num)) != null){
                pairs += mult;
            }

            putVal(seen, num+k);
            putVal(seen, num-k);

        }

        return pairs; 
        
    }
}