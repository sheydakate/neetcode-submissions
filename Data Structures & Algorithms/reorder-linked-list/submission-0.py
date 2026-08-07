class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def reorderList (self, head: ListNode)->None:
        #2 pointers to find mid of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #braking the list into two
        second = slow.next
        slow.next = None
        
        prev = None #random pointer for now
        
        #reverse second list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #merging the 2 lists
        first, second = head, prev #prev now holds the las node
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
    
    #T: O(n)
    #M: O(1)
    
    
#Test case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution ()
sol.reorderList(head)

#printing
current = head

while current:
    print(current.val, end="->" if current.next else"")
    current = current.next

    
    
        
        
        