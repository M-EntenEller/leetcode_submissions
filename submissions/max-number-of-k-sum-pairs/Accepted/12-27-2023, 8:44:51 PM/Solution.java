// https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution {
    public int maxOperations(int[] nums, int k) {

        Map<Integer, Integer> countMap = new HashMap<>();
        int res = 0; 

        for (int num: nums)
        {
            if (countMap.getOrDefault(k-num, 0) > 0){
                countMap.put(k-num, countMap.get(k-num) - 1);
                res++;
            } else {
                countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            }
        }

        return res; 
        
    }
}