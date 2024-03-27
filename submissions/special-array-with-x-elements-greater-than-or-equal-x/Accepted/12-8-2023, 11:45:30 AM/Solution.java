// https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x

class Solution {
    public int specialArray(int[] nums) {

        Arrays.sort(nums);
        int ng;

        for (int i=0; i<nums.length; i++)
        {
            ng = nums.length - i;

            if (nums[i] >= ng){

                if (i==0 || nums[i-1] < ng){
                    return ng;
                }
            
            }
        } 
        
        return -1;
        
    }
}