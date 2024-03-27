// https://leetcode.com/problems/maximum-number-of-pairs-in-array

class Solution {
    public int[] numberOfPairs(int[] nums) {
        
        int pairs = 0;
        int[] countMap = new int[101];

        for (int num: nums){

            countMap[num]++;

        }

        for (int i=0; i<countMap.length; i++){

            pairs += countMap[i] / 2;

        }

        return new int[]{pairs, nums.length - pairs*2};

    }
}