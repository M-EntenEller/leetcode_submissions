// https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum

import java.util.Arrays;

class Solution {

    public int[] maxSubsequence(int[] nums, int k) {

        int[] res = new int[k];

        for (int i=0; i<k; i++){
            res[i] = i;
        }

        for (int i=k; i < nums.length; i++){

            int tmp_min = Integer.MAX_VALUE;
            int tmp_idx = -1;

            for (int j=0; j<k; j++){
                
                if (nums[res[j]] < tmp_min){
                    tmp_min = nums[res[j]];
                    tmp_idx = j;
                }

            }

            if (nums[i] > tmp_min){
                res[tmp_idx] = i;
            }    

        }

        Arrays.sort(res);
        for (int i=0; i<k;i++){
            res[i] = nums[res[i]];
        }

        return res;
        
    }
}