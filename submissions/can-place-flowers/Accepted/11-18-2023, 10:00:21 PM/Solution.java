// https://leetcode.com/problems/can-place-flowers

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        int count = 0;
        int adjZeroes = 1;

        for (int i=0; i<flowerbed.length; i++){

            if (flowerbed[i] == 0){
                adjZeroes++;
            }else{
                adjZeroes = 0;
            }

            if(adjZeroes == 3){
                count++;
                adjZeroes = 1;
            }

        } 

        if (adjZeroes == 2){
            count++;
        }

        return count >= n;

    }
}