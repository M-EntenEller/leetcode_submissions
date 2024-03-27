// https://leetcode.com/problems/longest-subsequence-with-limited-sum

class Solution {

    public int floorBinarySearch(int[] arr, int target){
        
        int l = 0;
        int r = arr.length - 1;
        int mid = -1;

        while (l <= r){

            mid = l + (r-l)/2;
            int midVal = arr[mid];

            if (midVal == target){
                return mid;
            } else if (target < midVal){
                r = mid - 1;
            } else{ // target > midVal
                if (mid + 1 <= arr.length -1 && arr[mid+1] > target){
                    return mid;
                }
                l = mid + 1;
            }

        }

        if (r < 0){
            return -1;
        } 
        return mid;
    }

    public int[] answerQueries(int[] nums, int[] queries) {

        Arrays.sort(nums);
        int[] sumA = new int[nums.length];
        sumA[0] = nums[0];

        for (int i=1; i<nums.length; i++){
            
            sumA[i] = sumA[i-1] + nums[i];

        }

        for (int i=0; i<queries.length; i++){

            queries[i] = floorBinarySearch(sumA, queries[i]) + 1;

        }
        
        return queries;

    }
}