class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def maximum_twin_sum(self, head):
        fast= slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res