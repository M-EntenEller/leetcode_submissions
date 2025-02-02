// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def hb(node):
            
            if node == None: 
                return [1, True]

            l = hb(node.left)
            r = hb(node.right)
            child_good = l[1] and r[1]
            node_good = abs(l[0] - r[0]) <= 1
            
            return [max(l[0],r[0]) + 1, child_good and node_good]

        return hb(root)[1] 

        

            

        

        