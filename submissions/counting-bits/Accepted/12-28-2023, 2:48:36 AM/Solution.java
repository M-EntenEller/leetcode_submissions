// https://leetcode.com/problems/counting-bits

class Solution {

    private int bitCount(int x){
        
        int count = 0;

        while (x > 0)
        {
            count += x % 2;
            x = x/2;    
        }

        return count;

    }

    public int[] countBits(int n) {

        int[] res = new int[n+1];

        for(int i=0; i<=n; i++)
        {
            res[i] = bitCount(i);
        }

        return res;

    }
}