// https://leetcode.com/problems/mean-of-array-after-removing-some-elements

class Solution:
    def trimMean(self, arr: List[int]) -> float:
       
        n = len(arr)
        treshold = n // 20
        arr.sort()
        cut = arr[treshold : n - treshold]

        return sum(cut)/len(cut)