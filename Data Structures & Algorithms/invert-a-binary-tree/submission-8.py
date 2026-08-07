class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree (self, root:  TreeNode)-> TreeNode:
        
        def dfs(cur):       #recursion function
            if not cur:
                return      #edge case
            
            cur.left, cur.right = cur.right, cur.left  #switching L and R
            
            dfs(cur.left)   #recursive call
            dfs(cur.right)
            
            return cur  #return result
            
            
        return dfs(root)    #first line to execute
        
# T: O(n) visiting ery node to flip them
# S: O(h) h->height of tree 
#    Worst: O(n)  Best: O(log n)