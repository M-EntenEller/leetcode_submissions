// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i

class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {

        for (int i=0; i<nums.length - indexDifference; i++){

            for (int j=i+indexDifference; j<nums.length; j++){
                
                int absDiff = nums[i] > nums[j] ? nums[i] - nums[j] : nums[j] - nums[i];
                
                if (absDiff >= valueDifference){
                    return new int[]{i,j};
                }

            }

        }

        return new int[]{-1,-1};
        
    }
}