class ListNode:
    def __init__(self, next= None, val=0):
        self.val = val
        self.next = next

class Solution:
    def remove(self, head, val):

        dummy = ListNode(next =head)

        cur, prev = head, dummy
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)



    solution = Solution()
    res_list = solution.remove(head,2)


    while res_list:
        print(res_list.val, end=" -> ")
        res_list = res_list.next