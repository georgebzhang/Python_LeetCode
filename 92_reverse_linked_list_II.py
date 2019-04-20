class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        prev_m, head_m = None, head
        for _ in range(m-1):
            prev_m = head_m
            head_m = head_m.next

        prev, curr = prev_m, head_m
        for _ in range(n-m+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if prev_m:
            prev_m.next = prev
        else:
            head = prev
        head_m.next = curr

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
        m, n = 2, 4
        head = self.build_linked_list(vals)
        self.print_linked_list(head)
        ans = self.reverseBetween(head, m, n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
