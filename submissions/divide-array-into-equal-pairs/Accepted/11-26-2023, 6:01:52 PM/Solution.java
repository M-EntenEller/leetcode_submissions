// https://leetcode.com/problems/divide-array-into-equal-pairs

class Solution {
    public boolean divideArray(int[] nums) {
        
        Map<Integer,Integer> countMap = new HashMap<>();
        Integer tmp;

        for (int num: nums)
        {

            if ((tmp = countMap.get(num)) == null)
            {
                countMap.put(num, 1);
                continue;
            }

            tmp++;

            if (tmp % 2 == 0)
            {
                countMap.remove(num);   
            }
            else
            {
                countMap.put(num, tmp);
            }
            
        }

        return countMap.size() == 0;

    }
}