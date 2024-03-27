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

    private void setup(int[] a){
       
        u = Math.max(Math.max(a[0], a[1]), Math.max(a[1], a[2]));
        u3 = Math.min(Math.min(a[0],a[1]), Math.min(a[1], a[2]));
        u2 = a[0] + a[1] + a[2] - u - u3;
        l = u3;
        l2 = u2;

    }

    public int maximumProduct(int[] nums) {

        setup(nums);

        for (int i=3; i<nums.length; i++){

            updateUpper(nums[i]);
            updateLower(nums[i]);

        }


        return Math.max(l*l2*u, u*u2*u3);
        
    }
}