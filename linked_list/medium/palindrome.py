  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

 # TC-O(N), SC-O(N)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        stack=[]
        isPal=True
        while (slow is not None):
            stack.append(slow.val)
            slow=slow.next
        if stack==stack[::-1]:
            return True
        return False
      
# TC-O(N), SC-O(1)     
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head

        #find middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse from middle
        curr=slow
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        #check for palindrome if the same element exists in the linked list from the middle element.
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True



        
            

        
