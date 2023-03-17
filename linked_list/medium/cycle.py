# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# TC-O(N), SC-O(N)- extra space for hastable
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashTable=set()
        while head is not None:
            if head in hashTable:
                return True
            hashTable.add(head)
            head=head.next
        return False
      
      
 # TC-O(N), SC-O(1)- tortoise approach
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                return True
        return False
