class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next

class Solution:
    def mergelists(self, l1,l2):
        dummy =  ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next =l1
        elif l2:
            tail.next = l2

        return dummy.next



if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)


    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)


    solution = Solution()
    merged_list = solution.merge_lists(list1, list2)


    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
