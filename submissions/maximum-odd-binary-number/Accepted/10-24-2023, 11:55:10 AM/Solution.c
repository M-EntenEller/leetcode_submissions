// https://leetcode.com/problems/maximum-odd-binary-number

char* maximumOddBinaryNumber(char* s){

    int i = 0;
    int j = 0;

    while (s[i] != 0){
        
        if (s[i] == '1'){
            s[i] = '0';
            s[j] = '1';
            j++;
        }

        i++;

    }

    if (s[i-1] != '1'){
        s[i-1] = '1';
        s[j-1] = '0';
    }

    return s;

}