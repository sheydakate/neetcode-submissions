# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Base case
        if not lists:
            return None

        #going thru whole list
        while len(lists) > 1:
            tempMerge = []

            for i in range (0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                
                #Merge pairs
                tempMerge.append(self.mergeTwoLists(list1, list2))
            
            #now holds lists marged in pairs
            lists = tempMerge

        #lists = [[]]
        return lists[0]


    #Helper function to merge
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        temp = dummy

        #sort and merge
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        
        #attach remainig nodes in one list 
        temp.next = l1 if l1 else l2

        return dummy.next

# number of lists: k , number of total nodes: n
# T: O (n logk)
#while loop: O(log k) list is halved each time , for loop: O(k) visits all lists eventully, merge function: O(n) visists every node *** n >= k

# S: (k) for the temp array in while loop