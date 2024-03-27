// https://leetcode.com/problems/best-poker-hand

class Solution {

    public int kinds(int[] arr){

        int[] countMap = new int[14];
        int max_kinds = 0;

        for (int x: arr){

            max_kinds = ++countMap[x] > max_kinds ? countMap[x] : max_kinds;

        }

        return max_kinds;

    }

    public String bestHand(int[] ranks, char[] suits) {

        boolean flush = true;
        for(int i=1; i<suits.length; i++){
            if (! (suits[i-1] == suits[i])){
                flush = false;
                break;
            }
        }
        
        if (flush){
            return "Flush";
        }

        int max_kinds = kinds(ranks);

        if (max_kinds == 1){
            return "High Card";
        }

        if (max_kinds == 2){
            return "Pair";
        }

        return "Three of a Kind";
        
    }
}