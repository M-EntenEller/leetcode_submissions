// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

int minimumDifference(int* nums, int numsSize, int k) {

    int cursor = numsSize;
    int tmp;

    while (cursor > 0){

        for (int i=0; i<cursor-1; i++){

            if (nums[i] > nums[i+1]){
                tmp = nums[i+1];
                nums[i+1] = nums[i];
                nums[i] = tmp;
            }

        }

        cursor--;

    }

    int diff = nums[0 + k -1 ] - nums [0];

    for (int i=1; i<numsSize-k+1; i++){
        
        int next = nums[i+k-1] - nums[i];
        if (next < diff){
            diff = next;
        }

    }

    return diff; 
    
}