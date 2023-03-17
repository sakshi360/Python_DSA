# Reverse a Linked List
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Initialize three pointers prev as NULL, curr as head, and next as NULL.
Iterate through the linked list. In a loop, do the following:
Before changing the next of curr, store the next node 
next = curr -> next
Now update the next pointer of curr to the prev 
curr -> next = prev 
Update prev as curr and curr as next 
prev = curr 
curr = next
'''
#Iterative solution
# TC-O(N);SC-O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        return prev
      
#Recursive Solution
# TC-O(N);SC-O(N)
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        
        # Reverse the rest list
        revNode=self.reverseList(head.next)

        # Put first element at the end
        head.next.next=head
        head.next=None
        
        return revNode
