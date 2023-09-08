class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def intersect_node(self, headA, headB):
        l1,l2 = headA, headB
        while l1!=l2:
            l1= l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(9)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(4)


    head2 = ListNode(3)
    head2.next = ListNode(2)
    head2.next.next = ListNode(4)

    solution = Solution()
    intersect = solution.intersect_node(head, head2)
    print(intersect)

