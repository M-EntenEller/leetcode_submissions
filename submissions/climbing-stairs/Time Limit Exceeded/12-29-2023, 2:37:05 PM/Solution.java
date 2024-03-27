// https://leetcode.com/problems/climbing-stairs

class Solution {

    private int dps(int n){

        if (n==1){
            return 1;
        }

        if (n==2){
            return 2;
        }

        return dps(n-2) + dps(n-1);
    }

    public int climbStairs(int n) {

        return dps(n);
        
    }
}