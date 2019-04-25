class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        while True:
            ind_None = None
            try:
                ind_None = lists.index(None)
            except:
                break
            del lists[ind_None]

        head = ListNode(-1)  # dummy
        prev = head
        while lists:
            ind_min = lists.index(min(lists, key=lambda l: l.val))
            prev.next = ListNode(lists[ind_min].val)
            prev = prev.next
            lists[ind_min] = lists[ind_min].next
            if not lists[ind_min]:
                del lists[ind_min]

        return head.next

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
        l1_vals = [1, 4, 5]
        l2_vals = [1, 3, 4]
        l3_vals = [2, 6]
        l1_head = self.build_linked_list(l1_vals)
        l2_head = self.build_linked_list(l2_vals)
        l3_head = self.build_linked_list(l3_vals)
        lists = [l1_head, l2_head, l3_head]
        for l in lists:
            self.print_linked_list(l)
        ans = self.mergeKLists(lists)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
