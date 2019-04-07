class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(None)
        prev.next = head
        while prev.next and prev.next.next:
            # assigning n1, n2
            n1 = prev.next
            n2 = n1.next
            # reversing n1, n2
            n1.next = n2.next
            n2.next = n1
            # mutate node before n1
            prev.next = n2
            # advance prev
            prev = n1
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
        vals = [1, 2, 3, 4]
        head = self.build_linked_list(vals)
        self.print_linked_list(head)
        ans = self.swapPairs(head)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
