// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution {
    public int maxProfit(int[] prices, int fee) {
    
        int a[] = new int[prices.length];

        for (int i=1; i<prices.length; i++){

            int tmp = 0;

            for (int j=i; j>=0; j--){

                tmp = Math.max(prices[i] - prices[j] - fee, 0) + a[j>0 ? j-1 : 0];

                if(tmp > a[i]){
                    a[i] = tmp;
                }

            }

        }

        return a[prices.length-1];

    }

}