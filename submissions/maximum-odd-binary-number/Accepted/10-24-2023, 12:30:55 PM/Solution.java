// https://leetcode.com/problems/maximum-odd-binary-number

class Solution {
    public String maximumOddBinaryNumber(String s) {

        int n = s.length();
        char[] res = new char[n];
        int leads = -1;
        
        for(int i = 0; i<n; i++){

            if (s.charAt(i) == '1'){
                leads += 1;
            }

        }

        for (int i=0; i<n-1; i++){
            
            if (leads > 0){
                res[i] = '1';
                leads--;
            } else{
                res[i] = '0';
            }

        }

        res[n-1] = '1';

        return new String(res);
        
    }
}