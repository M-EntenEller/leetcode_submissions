// https://leetcode.com/problems/maximum-odd-binary-number

class Solution {
    public String maximumOddBinaryNumber(String s) {

        char[] tmp = new char[s.length()];

        for (int i=0; i < s.length(); i++){
            
            tmp[i] = s.charAt(i);

        }

        int j = 0;

        for (int i=0; i< s.length(); i++){
           
            if (tmp[i] == '1'){
                tmp[i] = '0';
                tmp[j] = '1';
                j++;
            }

        }

        if (tmp[s.length()-1] != '1'){
            tmp[s.length()-1] = '1';
            tmp[j-1] = '0';
        }

        return new String(tmp);
        
    }
}