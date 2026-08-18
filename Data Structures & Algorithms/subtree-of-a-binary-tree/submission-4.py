class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: treeNode, subroot: treeNode)->bool:

        #recursive call to check if same starting root
        def sameTree(p,q):

            if not p and not q: return True

            if not p or not q: return False

            if p.val != q.val: return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)


        if not subroot: return True

        if not root: return False

        if sameTree(root, subroot): return True

        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

# T: O(N*M)
# S: O(N+M)