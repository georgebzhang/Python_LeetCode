class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next  # save next
            curr.next = prev  # reverse
            prev = curr  # advance prev
            curr = next  # advance next
        return prev

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
        vals = [1, 2, 3, 4, 5]
        head = self.build_linked_list(vals)
        self.print_linked_list(head)
        ans = self.reverseList(head)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
