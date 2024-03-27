// https://leetcode.com/problems/maximum-number-of-balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = [0] * 5

        for c in text: 

            if c == "b":
                count[0] += 1
            elif c == "a":
                count[1] += 1
            elif c == "l":
                count[2] += 0.5
            elif c == "o":
                count[3] += 0.5
            elif c == "n":
                count[4] += 1

        return int(min(count))





            
             
        