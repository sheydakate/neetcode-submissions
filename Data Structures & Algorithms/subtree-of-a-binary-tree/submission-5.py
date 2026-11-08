# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        #found a matching subtree
        if self.sameTree(root, subRoot):
            return True
        
        #find a node that matches subroot
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    #Helper function to see if same tree
    def sameTree(self, root: TreeNode, subroot: TreeNode):
        if not root and not subroot:
            return True
        if root and subroot and root.val == subroot.val:
            return (self.sameTree(root.left, subroot.left) and           
                    self.sameTree(root.right, subroot.right))
        return False

# T: O(n + m)   n: nodes in root    m: nodes in subRoot 
# S: O(n + m)
