// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {

        HashSet<Integer> covered = new HashSet<>();
        int i=0;
        int[][] nums = ranges;

        while (covered.size() < right-left+1 && i<ranges.length){
            
            for (int j=left; j<=right; j++){

                if (nums[i][0] <= j && j <= nums[i][1]){
                    covered.add(j);
                }

            }

            i++;
        } 

        return covered.size() == right-left+1;
        
    }
}