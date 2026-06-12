# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev , curr = None , head
        while curr:
            nxt=curr.next #defining var
            curr.next=prev  #rev link
            prev=curr #moving pointer prev
            curr=nxt #moving pointer curr
        return prev    
        
        