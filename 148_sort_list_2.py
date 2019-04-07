class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge(self, l, r):
        dummy = tail = ListNode(None)  # must set dummy = tail so that changes to tail affect dummy
        while l and r:
            if l.val < r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        tail.next = l or r  # if either l or r is depleted
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # not head handles empty list input only
            return head

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next  # slow is start of second list
        prev.next = None  # truncate first

        return self.merge(*map(self.sortList, (head, slow)))  # * collects all arguments in a tuple

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
        vals = [4, 2, 1, 3]
        head = self.build_linked_list(vals)
        self.print_linked_list(head)
        ans = self.sortList(head)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
