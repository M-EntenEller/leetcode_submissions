// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        nh = len(haystack)
        nn = len(needle)

        for i in range(nh - nn + 1):

            count = 0

            for j in range(nn):

                if haystack[i+j] == needle[j]:
                    count +=1 
                    if count == nn:
                        return i
                else: 
                    count = 0 
                    break

        return -1
                     
