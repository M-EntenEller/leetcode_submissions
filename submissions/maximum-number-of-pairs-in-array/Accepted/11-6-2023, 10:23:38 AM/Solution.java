// https://leetcode.com/problems/maximum-number-of-pairs-in-array

class Solution {
    public int[] numberOfPairs(int[] nums) {
        
        int pairs = 0;
        Set<Integer> s = new HashSet<>();

        for(Integer num: nums){

            if (s.contains(num)){
                pairs++;
                s.remove(num);
            } else {
                s.add(num);
            }


        }

        return new int[]{pairs, nums.length - pairs*2};

    }
}