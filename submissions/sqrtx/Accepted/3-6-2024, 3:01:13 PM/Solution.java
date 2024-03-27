// https://leetcode.com/problems/sqrtx

class Solution {

    public int mySqrt(int x) {

        if (x<1){
            return 0;
        }

        long tmp = 0;
        
        for (long i=1; i*i <= x; i++)
        {
            tmp = i;
        }

        return (int)tmp;

    }
}