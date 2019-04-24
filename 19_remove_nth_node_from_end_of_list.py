class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # find total length
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next

        if length == 1:
            return None  # assuming n is always valid (n = 1 in this case)

        ptr = head
        before_remove = length-n-1
        if before_remove < 0:
            return head.next  # if head (first ListNode) is to be removed
        for _ in range(before_remove):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head

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
        n = 2
        head = self.build_linked_list(vals)
        self.print_linked_list(head)
        ans = self.removeNthFromEnd(head, n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
