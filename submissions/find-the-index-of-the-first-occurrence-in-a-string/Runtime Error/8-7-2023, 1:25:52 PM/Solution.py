// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nn = len(needle)
        nh = len(haystack)

        i = count = 0

        while i < nh-nn+1:
            
            for j in range(nn):
                
                if haystack[i+j] == needle[j]:
                    count += 1
                else: 
                    count = 0
                    i = i+j
                    if j == 0:
                        i += 1

                if count == nn:
                    return i
            
        return -1