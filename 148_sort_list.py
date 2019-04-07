class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = ptr = l
        l = l.next
        while l and r:
            if l.val < r.val:
                ptr.next = l
                l = l.next
            else:
                ptr.next = r
                r = r.next
            ptr = ptr.next
        ptr.next = l or r
        return head

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next  # start of second
        slow.next = None  # truncate first

        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

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
