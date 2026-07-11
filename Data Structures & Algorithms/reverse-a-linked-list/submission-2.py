# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None 
        curr = head

        while curr: # while this exists 

            temp = curr.next # set temp value to hold next value 
            curr.next = prev # the next value then bcomes None or prev
            prev = curr # Prev then becomes the head 
            curr = temp # then the head becomes the next value 

            # None -> 1(h) -> 2 -> 3 
            # None <- 1(prev) <- 2(head) -> 3 

        return prev 
            

        