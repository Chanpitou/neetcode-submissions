# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, node = 0, head
        while node:
            length += 1
            node = node.next

        nth = length - n
        if nth == 0:
            return head.next
        dummy = curr = head
        prev = ListNode()
        i = 0

        while curr:
            next_node = curr.next
            if i == nth:
                prev.next = next_node
                prev = prev.next
            else:
                prev = curr
            curr = next_node
            i += 1
        return dummy