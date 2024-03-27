// https://leetcode.com/problems/find-the-distinct-difference-array

class Solution {
    public int[] distinctDifferenceArray(int[] nums) {

        Set<Integer> preS = new HashSet<>();
        Set<Integer> sufS = new HashSet<>();
        int[] res = new int[nums.length];
        int[] sufA = new int[nums.length + 1];
        int count = 0;

        for (int i=0; i<nums.length; i++){

            if (!preS.contains(nums[i])){
                  preS.add(nums[i]);
                  count++;        
            }

            res[i] = count;

        }

        count = 0;

        for (int i=nums.length-1; i >= 0; i--){

            if (!sufS.contains(nums[i])){
                  sufS.add(nums[i]);
                  count++;        
            }

            sufA[i] = count;

        }

        for (int i=0; i<nums.length; i++){

            res[i] -= sufA[i+1];

        }
        
        return res;
    }
}