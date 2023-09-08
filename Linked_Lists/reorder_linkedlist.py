class ListNode:
    def __init__(self, val =0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reorder_linkedlist(self, head):
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        prev = slow.next = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

