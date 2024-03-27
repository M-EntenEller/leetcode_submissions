// https://leetcode.com/problems/maximum-product-of-three-numbers

class Solution {

    int u,u2,u3;
    int l,l2;

    private void updateUpper(int x){

        if (x > u){
            u3 = u2;
            u2 = u;
            u = x;
        }else if(x > u2){
            u3 = u2;
            u2 = x;
        } else if (x > u3){
            u3 = x;
        }

    }

    private void updateLower(int x){

        if (x < l){
            l2 = l;
            l = x;
        } else if(x < l2){
            l2 = x;
        }

    }

    public int maximumProduct(int[] nums) {

        u = u2 = u3 = Integer.MIN_VALUE;
        l = l2 = Integer.MAX_VALUE;

        for(int x: nums){

            updateUpper(x);
            updateLower(x);

        }


        return Math.max(l*l2*u, u*u2*u3);
        
    }
}