// https://leetcode.com/problems/fair-candy-swap

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        na = len(aliceSizes)
        nb = len(bobSizes)

        sA = sum(aliceSizes)
        sB = sum(bobSizes)

        r = (sA - sB) / 2

        for i in range(na):
            for j in range(nb):
                box_i = aliceSizes[i]
                box_j = bobSizes[j]
                if box_i - box_j == r:
                    return [box_i, box_j]        

        return None