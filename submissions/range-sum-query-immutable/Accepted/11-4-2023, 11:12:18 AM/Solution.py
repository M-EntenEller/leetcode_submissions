// https://leetcode.com/problems/range-sum-query-immutable

class NumArray:

    def __init__(self, nums: List[int]):

        self._arr = nums
        self.sa = []
        self.sa.append(0)
        _sum = 0

        for num in nums: 

            _sum += num
            self.sa.append(_sum)
        
    def sumRange(self, left: int, right: int) -> int:

        right += 1
        left += 1
        return self.sa[right] - self.sa[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)