# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = node = head
        while node:
            length += 1
            node = node.next
        
        indexToRemoved = length - n
        if indexToRemoved == 0:
            return dummy.next
        prev, curr = None, head
        i = 0
        while curr:
            next_node = curr.next
            if i == indexToRemoved:
                prev.next = next_node
                return dummy
            else:
                prev = curr
            curr = next_node
            i += 1
        return dummy