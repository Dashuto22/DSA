class ListNode:
    def __init__(self, val =0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middle_linked_list(self, head):

        fast=slow= head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    solution = Solution()
    mid = solution.middle_linked_list(head)

    print(mid.val)
