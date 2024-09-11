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


-----------------------

#just giving even list as head.next and doing the same thing as odd

class Solution:
   def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head: return None
       
       # odd points to the first node 
       odd = head
       # even points to the second node
       # evenHead will be used at the end to connect odd and even nodes
       evenHead = even = head.next
       
       # This condition makes sure odd can never be None, since the odd node will always be the one before the even node.
       # If even is not None, then odd is not None. (odd before even)
       # If even.next is not None, then after we update odd to the next odd node, it cannot be None. (The next odd node is even.next)
       while even and even.next:
           
           # Connect the current odd node to the next odd node
           odd.next = odd.next.next
           # Move the current odd node to the next odd node
           odd = odd.next
           
           #Same thing for even node
           even.next = even.next.next
           even = even.next
       
       # Connect the last odd node to the start of the even node
       odd.next = evenHead

       # head never changed, so return it
       return head
