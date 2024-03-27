// https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        js = set(jewels)
        res = 0

        for s in stones:
            if s in js:
                res += 1

        return res
        