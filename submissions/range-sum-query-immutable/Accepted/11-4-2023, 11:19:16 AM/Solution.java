// https://leetcode.com/problems/range-sum-query-immutable

class NumArray {

    int[] sumArray;

    public NumArray(int[] nums) {

        this.sumArray = new int[nums.length+1];
        
        for (int i=1; i<nums.length+1; i++){

            this.sumArray[i] = this.sumArray[i-1] + nums[i-1];

        }
    }
    
    public int sumRange(int left, int right) {
        
        return this.sumArray[right+1] - this.sumArray[left];

    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */