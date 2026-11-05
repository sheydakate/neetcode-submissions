class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[listNode])->None:
        #Base case
        if not head or not head.next:
            return
        
        #find middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #break into 2 list
        sec = slow.next
        slow.next = None

        #beginning of reversed second list
        prev = None

        #reverse list
        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp
        
        #new pointers for the beginning of the lists
        first = head
        second = prev

        #attach 2 lists
        while second: #bc if not equal, second list is shorter
            n1 = first.next
            n2 = second.next

            first.next = second
            second.next = n1

            first = n1
            second = n2

# T: O(n/2)+O(n/2)+O(n/2) = O(3n/2) = O(n) 
# S: O(1)
