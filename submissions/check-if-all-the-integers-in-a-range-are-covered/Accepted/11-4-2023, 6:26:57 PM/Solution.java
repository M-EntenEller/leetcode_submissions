// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {

        Set<Integer> covered = new HashSet<>();

        for (int i=0; i<ranges.length; i++){
            
            int lower = left < ranges[i][0] ? ranges[i][0] : left;
            int upper = right > ranges[i][1] ? ranges[i][1] : right;

            for (int j=lower; j<=upper; j++){
                covered.add(j);
            }

            if (covered.size() == right-left+1){
                return true;
            }
        
        }

        return false;
        
    }
}