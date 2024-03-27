// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing



int minOperations(int* nums, int numsSize){

    int res = 0;

    for (int i=1; i < numsSize; i++){

        if (nums[i] <= nums[i-1]){
            res += nums[i-1] + 1 - nums[i];
            nums[i] = nums[i-1] + 1;
        }

    }

    return res; 

}