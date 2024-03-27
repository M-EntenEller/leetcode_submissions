// https://leetcode.com/problems/image-smoother

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        n = len(img)
        m = len(img[0])
        cr = [-1, 0, 1]

        new_img = [[0]*m for _ in range(n)]

        for i in range(n):

            for j in range(m):

                _sum = 0
                items = 0

                for l in cr:

                    d1 = i + l
                    if not (0 <= d1 and d1 <=n-1):
                        continue

                    for k in cr:
                        
                        d2 = j+k
                        if not (0 <= d2 and d2 <=n-1):
                            continue

                        _sum += img[d1][d2]
                        items += 1

                new_img[i][j] = _sum // items  

        return new_img

                        
        