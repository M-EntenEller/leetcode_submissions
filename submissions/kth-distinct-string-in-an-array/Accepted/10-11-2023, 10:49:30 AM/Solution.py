// https://leetcode.com/problems/kth-distinct-string-in-an-array

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        m = {}
        for word in arr:
            if None == m.get(word):
                m[word] = 1
            else:
                m[word] += 1
                
        hits = 0

        for word in arr:

            if m.get(word) == 1:
                
                hits += 1
                if hits == k:
                    return word

        return ""
                
                