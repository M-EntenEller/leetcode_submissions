// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target

class Solution {
    public int countPairs(List<Integer> nums, int target) {

        int count = 0; 
        int left=0;
        int right=nums.size()-1;
        int[] numbers = nums.stream().mapToInt(Integer::intValue).toArray();

        Arrays.sort(numbers);
        
        while (left < right){

            if(numbers[left] + numbers[right] < target){
                count += right - left;
                left++;
            }else {
                right--;
            }

        }

        return count; 

    }
}