class ListNode:
    def __init__(self, val =0, next =None, random = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copylist(self, head):

        cur = head
        oldTocopy = {None: None}

        while cur:
            copy = ListNode(0)
            oldTocopy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = oldTocopy[cur]
            copy.next = oldTocopy[cur.next]
            copy.random = oldTocopy[cur.random]
            cur = cur.next

        return oldTocopy[head]