class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode)->bool:
        
        def dfs(p, q):
            
            if not p and not q: return True     #both empty: same
            
            if not p or not q: return False     #one empty
            
            if p.val != q.val: return False     #not empty but unmatching vals
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        return dfs(p, q)