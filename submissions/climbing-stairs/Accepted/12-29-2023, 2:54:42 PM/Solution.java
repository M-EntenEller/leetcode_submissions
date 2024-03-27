// https://leetcode.com/problems/climbing-stairs

class Solution {

    private int dps(int n, int[] memo){

        if (n<=2){
            return n;
        }

        int b1, b2;
        
        if ((b1=memo[n-2]) == 0){
            b1 = dps(n-1, memo);
        }
        
        if ((b2=memo[n-3]) == 0){
            b2 = dps(n-2, memo);
        }

        memo[n-1] = b1 + b2;
        return memo[n-1];

    }

    public int climbStairs(int n) {

        int[] memo = new int[n];

        return dps(n, memo);
        
    }
}