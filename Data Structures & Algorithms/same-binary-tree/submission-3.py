# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Base case 1
        if not p and not q:
            return True

        #Base case 2
        if not p or not q:
            return False

        #Base case 3
        if p.val != q.val:
            return False

        #Recursion call
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# T: O(n) compare up to every node in both trees
# S: O(h) recursion stack depends on height of the tree