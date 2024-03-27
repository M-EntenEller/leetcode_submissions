// https://leetcode.com/problems/find-the-maximum-divisibility-score

class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {

        int res = divisors[0];
        int max = 0;

        for (int i=0; i<divisors.length; i++)
        {
            int score = 0;

            for (int j=0; j<nums.length; j++)
            {
                if (nums[j]%divisors[i] == 0){
                    score++;
                }
            }

            if (score > max || (score == max && divisors[i] < res)){
                max = score;
                res = divisors[i];
            }
            
        }
        
        return res;
    }
}