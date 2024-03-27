// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

class Solution {
    public int minimumDifference(int[] nums, int k) {

        Arrays.sort(nums);
        int diff = nums[k-1] - nums[0];
        int tmp;

        for(int i=0; i<nums.length - k + 1; i++){

            tmp = nums[i+k-1] - nums[i];

            if (tmp < diff){
                diff = tmp;
            }

        }

        return diff;
        
    }
}