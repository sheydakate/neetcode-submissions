# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        walker = root

        while walker:

            if p.val > walker.val and q.val > walker.val:
                walker = walker.right
            
            elif p.val < walker.val and q.val < walker.val:
                walker = walker.left
            
            else:
                return walker

# T: O(h)   h = height of the tree
# S: O(1)
