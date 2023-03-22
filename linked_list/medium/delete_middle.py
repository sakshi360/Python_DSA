'''
delete middle of linked list -https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return
        prev=slow=fast=head
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head
