// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        bits = []
        tmp = head

        while tmp:

            bits.append(tmp.val)
            tmp = tmp.next

        
        n = len(bits)
        power = n - 1
        i = 0
        res = 0

        while i < n:

            res += bits[i] * 2**power   
            i += 1
            power -= 1 
            
        return res
             

            
            
        