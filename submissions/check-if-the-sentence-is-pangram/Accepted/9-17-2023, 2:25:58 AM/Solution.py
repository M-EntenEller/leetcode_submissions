// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        seen = set()

        for c in sentence:

            seen.add(c)

        return len(seen) == 26


            
            
        
        