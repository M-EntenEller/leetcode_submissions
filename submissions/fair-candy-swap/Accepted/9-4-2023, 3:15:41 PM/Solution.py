// https://leetcode.com/problems/fair-candy-swap

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        na = len(aliceSizes)
        nb = len(bobSizes)

        sA = sum(aliceSizes)
        sB = sum(bobSizes)

        r = (sA - sB) / 2 
        
        _m = {}
        for i in range(nb):
            box_i = bobSizes[i]
            _m[box_i + r] = box_i  

        for i in range(na):
            box_i = aliceSizes[i]
            match = _m.get(box_i)
            if match:
                return [box_i, match]

                

        