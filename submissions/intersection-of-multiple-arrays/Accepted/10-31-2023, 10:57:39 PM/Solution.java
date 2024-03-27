// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution {

    public List<Integer> intersection(int[][] nums) {

        int n = nums.length;
        int[] countMap = new int[1001];
        List<Integer> res = new ArrayList<Integer>();

        for (int i=0; i<n; i++){

            for (int j=0; j<nums[i].length; j++){

                countMap[nums[i][j]] += 1;

            }

        }

        for (int i=0; i<countMap.length; i++){
            
            if (countMap[i] == n){
                
                res.add((Integer) i);

            }

        }    

        return res;    

    }

}