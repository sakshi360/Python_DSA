'''' Problem Statement - find middle of linked list.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
  '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TC-O(n)+O(n/2)
# SC-O(1)

'''We can traverse through the Linked List while maintaining a count of nodes let’s say in variable n, and then traversing for 2nd time for n/2 nodes to get 
the middle of the list.
'''

class Solution1:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return

        a=head.next
        c=1

        while a is not None:
            a=a.next
            c=c+1
        
        mid=c//2+1
        for i in range (1,mid):
            head=head.next
        
        return head   
      

# TC-O(n/2)
# SC-O(1)
'''Tortoise Method
In the Tortoise-Hare approach, we increment slow ptr by 1 and fast ptr by 2, so if take a close look fast ptr will travel double that of the slow pointer.
So when the fast ptr will be at the end of the Linked List, slow ptr would have covered half of the Linked List till then.
So slow ptr will be pointing towards the middle of Linked List.'''

class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow,fast=head,head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow 
        
        
