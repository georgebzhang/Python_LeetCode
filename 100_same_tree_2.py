class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            # print('{}, {}'.format(p.val, q.val))
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if not p:
        #     return not q
        # if not q:
        #     return not p
        return p is q

    def print_answer(self, ans):
        print(ans)

    def test(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        ans = self.isSameTree(p, q)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
