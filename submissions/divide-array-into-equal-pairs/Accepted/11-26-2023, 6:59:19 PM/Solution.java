// https://leetcode.com/problems/divide-array-into-equal-pairs

class Solution {
    public boolean divideArray(int[] nums) {
        
        int[] count = new int[501];

        for (int num : nums)
        {
            count[num]++;
        }

        for (int c: count)
        {
            if (c == 0)
            {
                continue;
            }
            if (!(c % 2 == 0))
            {
                return false;
            }
        }

        return true;

    }
}