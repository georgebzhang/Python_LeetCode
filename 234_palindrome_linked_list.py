class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        def reverse(node):
            prev = None
            curr = node
            next = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid_rev = reverse(slow)
        start = head
        while mid_rev:
            if start.val != mid_rev.val:
                return False
            start = start.next
            mid_rev = mid_rev.next

        return True

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
        print(ans)

    def test(self):
        vals = [1, 2, 3, 2, 1]
        head = self.build_linked_list(vals)
        self.print_linked_list(head)
        ans = self.isPalindrome(head)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
