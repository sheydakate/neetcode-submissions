# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        #dfs
        def dfs(root, depth):
            #Base case
            if not root:
                return None
            
            #vising a level for the first time
            if len(res) == depth:
                res.append([])
            
            #adding node
            res[depth].append(root.val)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        #call dfs
        dfs(root, 0)
        return res

# T: O(n) n for all nodes
# S: O(n) n: all nodes , h: height for recursion 
#         O(n+h) = O(n)