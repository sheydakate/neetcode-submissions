class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd (self, head: ListNode, n = int)-> ListNode:
        dummy = ListNode(0, head)
        left = dummy   # by the time right reaches None, left is at one before n
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next
    
#T: O(n)
#M: O(1)

sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
n = 2

sol.removeNthFromEnd(head, n)


head2 = ListNode(4)
head2.next = ListNode(5)
n2 = 1

sol.removeNthFromEnd(head2, n2)

current = head
while current:
    print(current.val, end= "->" if current.next else "")
    current = current.next

print()
current2 = head2
while current2:
    print(current2.val, end= "->" if current2.next else "")
    current2 = current2.next

        
        