// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:

        lst = [c for c in str(num)]
        n = len(lst)
        res = 9999 + 1

        for i in range(n):
            
            for j in range(n):

                if j == i:
                    continue

                for l in range(n):

                    if l == i or l == j:
                        continue

                    for k in range(n):

                        if k == i or k == j or k == l:
                            continue

                        tmp = int(lst[i]) + int("".join([lst[j], lst[l], lst[k]]))
                        tmp2 = int("".join([lst[i], lst[j]])) + int("".join([lst[l], lst[k]]))

                        res = min(res, tmp, tmp2)

        return res

                        
        