class ListNode:
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next


class Solution:
    def reversell(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next =  ListNode(5)

    solution =  Solution()
    reversedll = solution.reversell(head)

    while reversedll:
        print(reversedll.val, end="->")
        reversedll = reversedll.next