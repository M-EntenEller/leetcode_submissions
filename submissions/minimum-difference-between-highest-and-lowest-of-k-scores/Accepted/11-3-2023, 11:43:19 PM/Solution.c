// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int minimumDifference(int* nums, int numsSize, int k) {

    int cursor = numsSize;
    int tmp;

    while (cursor > 0){

        for (int i=0; i<cursor-1; i++){

            if (nums[i] > nums[i+1]){
                swap(nums+i, nums+i+1);
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