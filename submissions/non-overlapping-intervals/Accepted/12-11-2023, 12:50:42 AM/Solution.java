// https://leetcode.com/problems/non-overlapping-intervals

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {

        int res = 0; 
        java.util.Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));

        int r = intervals[0][1];

        for (int i=1; i<intervals.length; i++)
        {
            if (intervals[i][0] < r){
                res++;
                r = Math.min(intervals[i][1], r);
            } else {
                r = intervals[i][1];
            }
        }

        return res;
    }
}