# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = [] #saves the node we pass so we can visit later
        curr = root #current node


        while curr or stack: #while we still have nodes (when first pushing) - or stack not empty (when popping)

            while curr:             # as long as curr not NULL
                stack.append(curr)  # add nodes to stack
                curr = curr.left    # go as far left as possible
                                    # last node added to the stack is the smallest node / top
            #cur is not NULL
            curr = stack.pop()      # saves the top node
            
            k -= 1 #reduce k 

            if k == 0:        # when we find our target
                return curr.val

            curr = curr.right   # if curr has a right child - we have to visit it - its children , if any, will be added to the top of the stack with whataver was previously in ther, be visited and popped 

# T: O(n) worst case
# S: o(h) height of a tree - reuse the same stack 

                        

        









# T: O(n)
# S: O(H)
