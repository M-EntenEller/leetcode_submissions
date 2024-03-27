// https://leetcode.com/problems/find-indices-with-index-and-value-difference-i

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findIndices(int* nums, int numsSize, int indexDifference, int valueDifference, int* returnSize) {
    
    int* res = (int*) malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i=0; i<numsSize - indexDifference; i++){

        for (int j = i + indexDifference; j<numsSize; j++){

            int diff = nums[i] - nums[j];
            if (diff < 0){
                diff = -diff;
            }

            if (diff >= valueDifference){
                res[0] = i;
                res[1] = j;
                return res;
            }

        }

    }

    res[0] = -1;
    res[1] = -1;
    return res;

}