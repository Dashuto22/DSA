class ListNode:
    def __init__(self, val =0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_duplicate(self, head):
        curr = head

        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next

            curr = curr.next

        return head

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)



    solution = Solution()
    res_list = solution.remove_duplicate(head)


    while res_list:
        print(res_list.val, end=" -> ")
        res_list = res_list.next