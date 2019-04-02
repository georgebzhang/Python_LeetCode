class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        def list_traversal(n):
            def traversal(n):
                if n is None:
                    l.append('null')
                else:
                    l.append(n.val)
                    traversal(n.left)
                    traversal(n.right)

            l = []
            traversal(n)
            return l

        l_p = list_traversal(p)
        l_q = list_traversal(q)

        return l_p == l_q

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
