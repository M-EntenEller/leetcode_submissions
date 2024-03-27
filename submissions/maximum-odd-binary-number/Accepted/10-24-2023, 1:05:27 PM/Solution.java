// https://leetcode.com/problems/maximum-odd-binary-number

class Solution {
    public String maximumOddBinaryNumber(String s) {

        char[] tmp = new char[s.length()];
        int j = 0;

        for (int i=0; i < s.length(); i++){
           
            if (s.charAt(i) == '1'){
                tmp[i] = '0';
                tmp[j] = '1';
                j++;
            } else{
                tmp[i] = '0';
            }

        }

        if (tmp[s.length()-1] != '1'){
            tmp[s.length()-1] = '1';
            tmp[j-1] = '0';
        }

        return new String(tmp);
        
    }
}