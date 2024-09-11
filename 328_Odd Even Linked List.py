# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: #empty list
            return head
            
        fast=head
        curr=head

        list2=ListNode() # to get even list
        curr2=list2

        while fast and fast.next:

            #for even
            curr2.next=curr.next
            curr2=curr2.next
            
            #for odd
            fast=fast.next.next #if odd its none
            curr.next=fast 
            curr=fast

        curr2.next=None #curr of even node should have none end as we took base as odd nodes
        

        #merging head and list2
        current=head
        while current.next:
            current=current.next
        current.next =list2.next

        return head
        
