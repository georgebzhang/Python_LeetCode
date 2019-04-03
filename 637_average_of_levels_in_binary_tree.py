from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def average(self, l):
        return sum(l) / len(l)

    def averageOfLevels(self, root):
        def level_order_traversal(n):
            q = deque()
            q.append(n)
            levels_list = []
            while q:
                level_list = []
                for i in range(len(q)):  # range fixed to length of q at this specific time
                    n = q.popleft()
                    level_list.append(n.val)
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                levels_list.append(level_list)

            return levels_list

        levels_list = level_order_traversal(root)
        levels_mean = [self.average(l) for l in levels_list]
        return levels_mean

    def print_answer(self, ans):
        print(ans)

    def test(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        r = root.right = TreeNode(20)
        r.left = TreeNode(15)
        r.left = TreeNode(7)
        ans = self.averageOfLevels(root)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
