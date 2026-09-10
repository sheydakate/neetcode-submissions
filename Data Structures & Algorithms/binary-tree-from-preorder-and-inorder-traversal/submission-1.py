# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # makes a hashmap with values:index - short version
        inorderIndex = {val: i for i, val in enumerate(inorder)}

        # points to the next root in preorder
        preIndex = 0

        def build (left, right): #indeces in the inorder - left/right subtree

            nonlocal preIndex # nonlocal means change the preIndex outside the function, dotn create a new one  

            # left and right cross- base case to break 
            if left > right:
                return None

            #Preorder always gives the root first
            rootVal = preorder[preIndex]
            preIndex += 1

            root = TreeNode(rootVal)

            # find where the root splits inorder
            mid = inorderIndex[rootVal]

            # build left subtree, then right subtree
            root.left = build(left, mid -1)
            root.right = build(mid + 1, right)

            return root


        return build (0, len(inorder) -1) # use indeces through 0 and 3    this starts with digit 4
        