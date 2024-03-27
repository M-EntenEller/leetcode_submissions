// https://leetcode.com/problems/check-if-the-sentence-is-pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alphabet_size = ord('z') -ord('a') + 1
        count_map = [0] * alphabet_size

        for c in sentence:
            
            key = ord(c) - ord("a")
            if count_map[key] == 0:
                count_map[key] = 1

        i = 0
        while i < alphabet_size:
            
            if not (count_map[i] > 0):
                return False
            i += 1

        return True


            
            
        
        