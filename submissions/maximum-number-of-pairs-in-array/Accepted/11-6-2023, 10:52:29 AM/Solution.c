// https://leetcode.com/problems/maximum-number-of-pairs-in-array

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfPairs(int* nums, int numsSize, int* returnSize) {

    #define VAL_BOUND 101
    int* res = (int*) malloc(2 * sizeof(int));
    *returnSize = 2;
    int pairs = 0;
    
    int countMap[VAL_BOUND];
    for(int i=0; i<VAL_BOUND; i++){
        countMap[i] = 0;
    }

    for (int i=0; i<numsSize; i++){

        countMap[nums[i]]++;

    }

    for (int i=0; i<VAL_BOUND; i++){

        pairs += countMap[i] / 2;

    }

    res[0] = pairs;
    res[1] = numsSize - pairs*2;

    return res;
    
}