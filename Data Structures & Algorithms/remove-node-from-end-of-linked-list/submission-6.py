class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #in case of removing head
        dummy = ListNode(0, head)

        slow = fast = dummy

        #move fast until it reaches the node after target -> n+1
        for _ in range(n+1):
            fast = fast.next
        
        #once fast reaches None, slow stops right before n from last
        while fast:
            slow = slow.next 
            fast = fast.next
        
        #remove the node
        slow.next = slow.next.next

        return dummy.next

# T: O(n) fast visits every node once
# S: O(1)