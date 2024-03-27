// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        if root==None:
            return -1 

        _min = root.val
        res = 2**31
        stack = [root]
        
        while stack:
            
            tmp = stack.pop()
            if tmp.val > _min and tmp.val < res: 
                res = tmp.val

            if tmp.left:
                stack.append(tmp.left)
            if tmp.right: 
                stack.append(tmp.right)

        return res if res < 2**31 else -1

            

            

            
            
        
        
        