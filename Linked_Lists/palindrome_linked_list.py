class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self,head):

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)


    solution = Solution()
    pal_list = solution.isPalindrome(head)

    print(pal_list)