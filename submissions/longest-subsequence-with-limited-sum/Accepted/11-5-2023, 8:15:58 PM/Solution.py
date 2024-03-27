// https://leetcode.com/problems/longest-subsequence-with-limited-sum

class Solution:

    def binary_search(self, target, A):

        l = 0
        r = len(A) - 1

        while l <= r:

            mid = l + (r-l)//2

            if target == A[mid]:    
                return mid
            elif target < A[mid]:
                r = mid - 1
            else: #target > A[mid]
                if mid+1 <= len(A)-1 and A[mid+1] > target:
                    return mid
                l = mid + 1

        if mid == 0 and A[0] > target:
            return -1 
        else: 
            return mid

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        sumA = [nums[0]]
        answer = []

        for i in range(1, len(nums)):

            sumA.append(sumA[i-1] + nums[i])

        for query in queries:
            
            answer.append(self.binary_search(query, sumA) + 1)

        return answer
        
