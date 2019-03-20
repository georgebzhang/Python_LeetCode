class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        def preorderTraversal_rec(root):
            result.append(root.val)
            if root.left:
                preorderTraversal_rec(root.left)
            if root.right:
                preorderTraversal_rec(root.right)

        result = []
        preorderTraversal_rec(root)
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
