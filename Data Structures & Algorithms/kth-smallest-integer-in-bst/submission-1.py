# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #store node vals in a list
        arr = []

        def inorder(root):
            if not root:
                return
            
            #inorder traversal
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)

        #return kth smallest index 
        return arr[k-1]

# T: O(n) n for all nodes
# S: O(n) n for arr **O(n)+O(h) = O(n)**