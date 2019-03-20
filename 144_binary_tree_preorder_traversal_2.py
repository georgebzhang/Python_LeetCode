class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        stack = []
        stack.append(root)

        while stack:
            n = stack.pop()
            result.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        root = TreeNode(1)
        node2 = TreeNode(2)
        root.right = node2
        node3 = TreeNode(3)
        node2.left = node3
        ans = self.preorderTraversal(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
