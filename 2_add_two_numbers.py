class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def linked_list_to_array(self, l):
        arr = []
        while True:
            arr.append(l.val)
            if l.next is None:
                break
            l = l.next
        return arr

    def array_to_value(self, arr):
        val = 0
        for i in range(len(arr)):
            val = val * 10 + arr[i]
        return val

    def value_to_array(self, val):
        arr = []
        while True:
            arr.append(val % 10)
            val = val // 10
            if val == 0:
                break
        return arr

    def array_to_linked_list(self, arr):
        l = None
        prev = None
        for i in range(len(arr)):
            l = ListNode(arr[i])
            l.next = prev
            prev = l
        return l

    def addTwoNumbers(self, l1, l2):
        arr1 = self.linked_list_to_array(l1)
        arr2 = self.linked_list_to_array(l2)
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        val1 = self.array_to_value(arr1)
        val2 = self.array_to_value(arr2)
        val_total = val1 + val2
        arr_total = self.value_to_array(val_total)
        arr_total = arr_total[::-1]
        l_total = self.array_to_linked_list(arr_total)
        return l_total

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
