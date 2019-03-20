from collections import deque


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []

        dq = deque()
        dq.append(root)

        while dq:
            temp = []
            for i in range(len(dq)):
                n = dq.popleft()
                temp.append(n.val)
                dq.extend(n.children)

            result.append(temp)

        return result

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
