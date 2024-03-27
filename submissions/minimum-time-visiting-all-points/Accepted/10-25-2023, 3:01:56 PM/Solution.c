// https://leetcode.com/problems/minimum-time-visiting-all-points

int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize){

    int res = 0;
    int* tmp = points[0];

    for (int i=1; i < pointsSize; i++){

        int* p = points[i];

        int d_x  = tmp[0] - p[0];
        int d_y  = tmp[1] - p[1];

        if (d_x < 0){d_x = -1*d_x;}
        if (d_y < 0){d_y = -1*d_y;}

        if (d_x > d_y){
            res += d_x;
        } else{
            res += d_y;
        }

        tmp = p;
    }

    return res;

}