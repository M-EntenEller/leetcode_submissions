// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words

class Solution {

    private int numericalValue(String s){

        int agg = 0; 

        for (int i=0; i<s.length(); i++){

            agg = agg * 10;
            agg += s.charAt(i) - 'a';
            
        }

        return agg;

    }

    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        
        int a = numericalValue(firstWord);
        int b = numericalValue(secondWord);
        int c = numericalValue(targetWord);

        return a+b==c;

    }
}