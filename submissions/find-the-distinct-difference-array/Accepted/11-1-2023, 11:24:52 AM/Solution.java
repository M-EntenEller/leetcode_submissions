// https://leetcode.com/problems/find-the-distinct-difference-array

class Solution {
    public int[] distinctDifferenceArray(int[] nums) {

        Set<Integer> preS = new HashSet<>();
        Set<Integer> sufS = new HashSet<>();
        int[] preA = new int[nums.length];
        int[] sufA = new int[nums.length + 1];
        int preC = 0;
        int sufC = 0; 
        int[] res = new int[nums.length];

        for (int i=0; i<nums.length; i++){

            if (!preS.contains(nums[i])){
                  preS.add(nums[i]);
                  preC++;        
            }

            preA[i] = preC;

        }

        for (int i=nums.length-1; i >= 0; i--){

            if (!sufS.contains(nums[i])){
                  sufS.add(nums[i]);
                  sufC++;        
            }

            sufA[i] = sufC;

        }

        for (int i=0; i<nums.length; i++){

            res[i] = preA[i] - sufA[i+1];

        }
        
        return res;
    }
}