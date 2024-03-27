// https://leetcode.com/problems/maximum-odd-binary-number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        res = []
        n = len(s)
        leads = -1

        for c in s:

            if c == "1":
                leads += 1

        return "".join(["1"] * (leads) + ["0"] * (n-leads-1) + ["1"])