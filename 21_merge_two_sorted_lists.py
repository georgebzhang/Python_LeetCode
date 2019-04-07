class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = tail = ListNode(None)  # must set dummy = tail so that changes to tail affect dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def build_linked_list(self, vals):
        head = ListNode(vals[0])
        prev = head
        for i in range(1, len(vals)):
            curr = ListNode(vals[i])
            prev.next = curr
            prev = curr
        return head

    def print_linked_list(self, head):
        ptr = head
        while ptr:
            print(ptr.val, ' ', end='')
            ptr = ptr.next
        print()

    def print_ans(self, ans):
        self.print_linked_list(ans)

    def test(self):
        l1_vals = [1, 2, 4]
        l2_vals = [1, 3, 4]
        l1 = self.build_linked_list(l1_vals)
        l2 = self.build_linked_list(l2_vals)
        self.print_linked_list(l1)
        self.print_linked_list(l2)
        ans = self.mergeTwoLists(l1, l2)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
