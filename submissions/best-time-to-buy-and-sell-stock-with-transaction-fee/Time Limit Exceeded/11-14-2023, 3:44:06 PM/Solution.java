// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution {
    public int maxProfit(int[] prices, int fee) {
    
        return _maxProfit(0, prices.length-1, prices, fee);

    }

    private int _maxProfit(int i, int j, int[] arr, int fee){

        if (i >= j){
            return 0;
        }

        int max = 0;

        for (int k=i; k<=j; k++){

            int intervalProfit = Math.max(arr[k] - arr[i] - fee, 0);
            int maxRemaining = _maxProfit(k+1, arr.length-1, arr, fee);
            int tmp = intervalProfit + maxRemaining;
            
            if(tmp > max){
                max = tmp;
            }

        }

        return max; 

    }
}