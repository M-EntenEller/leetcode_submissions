// https://leetcode.com/problems/reverse-bits

public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {

      int[] bitArr = new int[32];
      int res;

      for (int i=0; i<32; i++)
      {
        bitArr[i] = n & 1;
        n >>= 1;
      }

      res = bitArr[0];

      for (int i = 1; i < 32; i++)
      {
        res <<= 1;
        res += bitArr[i]; 
      }
        
      return res;
    }
}