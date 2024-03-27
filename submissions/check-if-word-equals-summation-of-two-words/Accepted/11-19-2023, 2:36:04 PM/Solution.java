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

    private int nV2(String s){

        return s.chars().reduce(0, (a,b) -> a*10 + (b - 'a'));

    }

    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        
        int a = nV2(firstWord);
        int b = nV2(secondWord);
        int c = nV2(targetWord);

        return a+b==c;

    }
}