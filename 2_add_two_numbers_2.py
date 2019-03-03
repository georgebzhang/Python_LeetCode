class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_by_digit(self, l1, l2, carry):
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)
        l = ListNode((l1.val + l2.val + carry) % 10)
        carry = (l1.val + l2.val + carry) // 10
        if l1.next is not None or l2.next is not None or carry == 1:
            l.next = self.add_by_digit(l1.next, l2.next, carry)
        return l

    def addTwoNumbers(self, l1, l2):
        l_total = self.add_by_digit(l1, l2, 0)
        return l_total

    def array_to_linked_list(self, arr):
        prev = None
        for i in range(len(arr)):
            n = ListNode(arr[i])
            n.next = prev
            prev = n
        return n

    def print_answer(self, ans):
        while True:
            print(ans.val, " ", end="")
            if ans.next is None:
                break
            ans = ans.next
        print()

    def test(self):
        l1 = self.array_to_linked_list([2, 4, 3])
        l2 = self.array_to_linked_list([5, 6, 4])
        ans = self.addTwoNumbers(l1, l2)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
