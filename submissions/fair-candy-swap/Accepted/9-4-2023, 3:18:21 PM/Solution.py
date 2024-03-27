// https://leetcode.com/problems/fair-candy-swap

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        r = (sum(aliceSizes) - sum(bobSizes)) / 2 
        
        _m = {}
        for box in bobSizes:    
            _m[box + r] = box  

        for box in aliceSizes:
            match = _m.get(box)
            if match:
                return [box, match]

                

        