// https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def leaf_sequence(root):

        if not root: 
            return []

        if not root.left and not root.right:
            return [root.val]

        return Solution.leaf_sequence(root.left) + Solution.leaf_sequence(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        s1 = Solution.leaf_sequence(root1)
        s2 = Solution.leaf_sequence(root2)

        if len(s1) != len(s2):
            return False

        for i in range(len(s1)):

            if s1[i] != s2[i]:
                return False

        return True
        
        