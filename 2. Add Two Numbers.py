# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # def reverse(ll):
        #     prev=None
        #     current=ll

        #     while current:
        #         next_=current.next
        #         current.next=prev
        #         prev=current
        #         current=next_
            
        #     return prev

        rl1=l1
        rl2=l2

        #final result in r2
        carry=0
        head1=rl1
        head2=rl2

        #checking if both list are of same size
        while rl1.next or rl2.next:
            if not rl1.next and rl2.next:
                rl1.next= ListNode()
            elif not rl2.next and rl1.next:
                rl2.next= ListNode()
            rl1=rl1.next
            rl2=rl2.next
        
        
        rl1=head1
        rl2=head2

        while rl1 and rl2:
            
            if rl1.val+rl2.val + carry <=9:
                rl2.val = rl1.val+rl2.val +carry
                carry=0 #done with this carry
                
            else:
                
                # carry = (rl1.val+rl2.val+carry) // 10 --first digit
                # rl2.val = (rl1.val+rl2.val+carry) % 10 --last digit
                value= str(rl1.val+rl2.val+carry)
             

                carry, rl2.val = int(value[0]),int(value[1])

                
            if not rl2.next and carry!=0:
                rl2.next= ListNode(carry,None)

            rl1=rl1.next
            rl2=rl2.next
        
        return head2
  ##############################################################################################

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        carry=0
        curr=dummy

        while l1 or l2 or carry!=0:
            digit1=l1.val if l1 else 0 --just give value zero , rather than assigning a listnode(0,node)
            digit2=l2.val if l2 else 0

            sum=digit1+digit2+carry
            digit=sum%10
            carry=sum//10

            curr.next=ListNode(digit)
            curr=curr.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return dummy.next

