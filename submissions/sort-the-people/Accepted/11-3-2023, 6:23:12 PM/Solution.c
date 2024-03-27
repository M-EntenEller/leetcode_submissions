// https://leetcode.com/problems/sort-the-people

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void swapInt(int i, int j, int* a){
    int tmp = a[j];
    a[j] = a[i];
    a[i] = tmp;
    return; 
}
void swapCharPointer(int i, int j, char**a){
    char* tmp = a[j];
    a[j] = a[i];
    a[i] = tmp;
    return;
}

char** sortPeople(char** names, int namesSize, int* heights, int heightsSize, int* returnSize) {

    char** res = (char**) malloc(sizeof(*res)*namesSize);
    int idx = namesSize-1;

    while (idx >= 0){

        int min = 1 << 30;
        int min_idx;

        for (int i=0; i<=idx; i++){

            if (heights[i] < min){
                min = heights[i];
                min_idx = i;
            }

        }

        swapInt(min_idx, idx, heights);
        swapCharPointer(min_idx, idx, names);
        res[idx] = names[idx]; 
        idx--;

    }

    *returnSize = namesSize;
    return res;
    
}