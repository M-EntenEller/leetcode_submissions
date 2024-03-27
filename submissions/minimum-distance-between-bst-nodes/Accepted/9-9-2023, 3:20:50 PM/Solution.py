// https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def min_diff(root, seen):

            if root == None:
                return None

            m = None

            for x in seen:

                diff = abs(root.val - x)

                if m == None or diff < m:
                    m = diff

            new_seen = seen.copy()
            new_seen.add(root.val)
            candidates = [m, 
                          min_diff(root.left, new_seen), 
                          min_diff(root.right, new_seen)]

            return min([x for x in candidates if x])

        return min_diff(root, set())
            
                


            



        

    
        