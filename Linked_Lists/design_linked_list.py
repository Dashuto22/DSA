class ListNode:
    def __init__(self, val =0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index):
        cur = self.left.next

        while cur and index >0:
            index -=1
            cur = cur.next

        if cur and cur != self.right and index ==0:
            return cur.val
        return -1

    def addAtHead(self, val):
        node, prev, next = ListNode(val), self.left, self.left.next

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


    def addAtTail(self, val):
        node, prev, next = ListNode(val), self.right.prev, self.right

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


    def addAtindex(self, index, val):
        cur = self.left.next

        while cur and index >0:
            index -=1
            cur = cur.next

        if cur and index ==0:
            node, prev, next = ListNode(val), cur.prev , cur
            prev.next = node
            next.prev = node
            node.next = next
            node.prev =prev

    def deleteAtindex(self, index):
        cur = self.left.next

        while cur and index >0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index==0:
            prev, next = cur.prev, cur.next

            prev.next = next
            next.prev =prev