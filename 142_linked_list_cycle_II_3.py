class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # if cycle exists
                slow = head
                while fast:
                    if slow is fast:
                        return slow
                    slow, fast = slow.next, fast.next

        return None

    def print_answer(self, ans, head):
        ind = 0
        ptr = head
        while ptr:
            if ans is ptr:
                break
            ind += 1
            ptr = ptr.next
        print('tail connects to node index {}'.format(ind))

    def build_linked_list(self, vals, pos):
        n = len(vals)
        head = ListNode(vals[0])
        prev = head
        for i in range(1, n):
            curr = ListNode(vals[i])
            prev.next = curr
            prev = curr
            if i == n-1:  # tail
                if pos != -1:
                    loop = head
                    for i in range(pos):
                        loop = loop.next
                    curr.next = loop
        return head

    def print_linked_list(self, head):
        ptr = head
        while ptr:
            print(ptr.val, ' ', end='')
            ptr = ptr.next
        print()

    def test(self):
        vals = [3, 2, 0, -4]
        pos = 1
        head = self.build_linked_list(vals, pos)
        # self.print_linked_list(head)
        ans = self.detectCycle(head)
        self.print_answer(ans, head)


if __name__ == '__main__':
    s = Solution()
    s.test()
