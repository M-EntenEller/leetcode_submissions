// https://leetcode.com/problems/climbing-stairs

class Solution {

    public int climbStairs(int n) {

        if (n<2){
            return n;
        }

        int b2 = 1;
        int b1 = 2;
        int tmp;

        for (int i=2; i<n; i++)
        {
            tmp = b1;
            b1 = b2 + b1;
            b2 = tmp;
        }
        
        return b1;
    }
}