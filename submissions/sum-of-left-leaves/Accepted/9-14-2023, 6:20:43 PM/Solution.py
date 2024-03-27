// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def bf(node, is_left):

            if not node:
                return 0
            
            if (not (node.left or node.right)) and is_left:

                return node.val

            return bf(node.left, True) + bf(node.right, False) 

        return bf(root, is_left=False)