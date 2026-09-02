# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort = head
        rabbit = head
        while rabbit is not None and rabbit.next is not None:
            tort = tort.next
            rabbit = rabbit.next.next
            if tort == rabbit:
                return True 

        return False 
        