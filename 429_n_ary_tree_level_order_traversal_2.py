from collections import deque


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        pass

    def print_answer(self, ans):
        print(ans)

    def test(self):
        children3 = [Node(5, []), Node(6, [])]
        children1 = [Node(3, children3), Node(2, []), Node(4, [])]
        root = Node(1, children1)
        ans = self.levelOrder(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
