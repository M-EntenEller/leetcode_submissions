// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

bool isCovered(int** ranges, int rangesSize, int* rangesColSize, int left, int right) {
    
    for (int i = left; i<=right; i++){

        char flag = 0;

        for (int j=0; j<rangesSize; j++){

            if (ranges[j][0] <= i && i <= ranges[j][1]){
                flag = 1;
            }

        }

        if (!flag){
            return 0;
        }

    }

    return 1;

}