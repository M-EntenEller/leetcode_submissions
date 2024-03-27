// https://leetcode.com/problems/range-sum-query-immutable




typedef struct {
    int* sa;
} NumArray;


NumArray* numArrayCreate(int* nums, int numsSize) {
    
    int* a = (int*) malloc(sizeof(int)*(numsSize+1));
    a[0] = 0;
    
    for (int i=1; i<numsSize+1; i++){
        
        a[i] = a[i-1] + nums[i-1];

    }

    NumArray* res = (NumArray*) malloc(sizeof(NumArray));
    res->sa = a;
    return res;
}

int numArraySumRange(NumArray* obj, int left, int right) {
    
    return obj->sa[right+1] - obj->sa[left];

}

void numArrayFree(NumArray* obj) {

    free(obj->sa);
    free(obj);
    
}

/**
 * Your NumArray struct will be instantiated and called as such:
 * NumArray* obj = numArrayCreate(nums, numsSize);
 * int param_1 = numArraySumRange(obj, left, right);
 
 * numArrayFree(obj);
*/