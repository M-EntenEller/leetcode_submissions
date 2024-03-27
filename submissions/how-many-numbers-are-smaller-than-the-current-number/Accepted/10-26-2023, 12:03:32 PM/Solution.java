// https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        
        int[] a = new int[101];

        for (int i=0; i < nums.length; i++){
            a[nums[i]] += 1;
        }

        int count = 0;

        for (int i = 0; i < a.length; i++){

            if(a[i] > 0){
                int tmp = a[i];
                a[i] = count;
                count += tmp;
            }

        }
        
        for (int i=0; i<nums.length; i++){
            
            nums[i] = a[nums[i]];

        }

        return nums;

    }
}