// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution {
    public int maximumProduct(int[] nums) {

        int max = Integer.MIN_VALUE; 
        int tmp;

        for (int i=0; i<nums.length-2; i++){

            for(int j=i+1; j<nums.length-1; j++){

                for(int k=j+1; k<nums.length; k++){

                    if ( (tmp = nums[i]*nums[j]*nums[k]) > max){
                        max = tmp;
                    }

                }

            }

        }

        return max;
        
    }
}