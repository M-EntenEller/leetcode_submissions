// https://leetcode.com/problems/maximum-product-difference-between-two-pairs

class Solution {
    public int maxProductDifference(int[] nums) {

        int a,b;
        int c,d;
        a = b = 0;
        c = d = (int) Integer.MAX_VALUE;

        for (int i=0; i<nums.length; i++){

            if (nums[i] > a){
                b = a;
                a = nums[i];
            } else if (nums[i] > b){
                b = nums[i];
            }

            if (nums[i] < c){
                d = c;
                c = nums[i];
            } else if (nums[i]<d){
                d = nums[i];
            }

        }

        return a*b - c*d;
        
    }
}