class ListNode:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def hash(self, key):
        return key % len(self.set)

    def add(self, key):
        cur =  self.set[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next

        cur.next = ListNode(key)

    def remove(self, key):
        cur = self.set[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next



    def contains(self, key):

        cur = self.set[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next

        return False