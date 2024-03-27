// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution {
    public boolean isCovered(int[][] ranges, int left, int right) {

        int[] line = new int[52];

        for(int[] range : ranges){

            line[range[0]]++;
            line[range[1]+1]--;

        }

        for (int i=0, overlap=0; i<=right; i++){

            overlap += line[i];
            
            if (i>=left && overlap == 0){
                return false;
            }

        }

        return true;
        
    }
}