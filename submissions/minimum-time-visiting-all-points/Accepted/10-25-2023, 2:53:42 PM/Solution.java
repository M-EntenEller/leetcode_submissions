// https://leetcode.com/problems/minimum-time-visiting-all-points

class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {

        int res = 0;
        int[] tmp = points[0];

        for (int i=1; i < points.length; i++){

            int[] p = points[i];
            int d_x = (tmp[0] - p[0]) > 0 ? (tmp[0] - p[0]) : -(tmp[0] - p[0]);
            int d_y = (tmp[1] - p[1]) > 0 ? (tmp[1] - p[1]) : -(tmp[1] - p[1]);
            
            int d;
            if (d_x > d_y){
                d = d_x;
            } else{
                d = d_y;
            }

            res += d;
            tmp = p;
        }

        return res;
        
    }
}