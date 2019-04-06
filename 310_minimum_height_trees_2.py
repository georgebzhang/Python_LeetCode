class Solution(object):
    def findMinHeightTrees(self, n, edges):
        g = [set() for _ in range(n)]  # graph
        for v1, v2 in edges:
            g[v1].add(v2)
            g[v2].add(v1)

        q, nq = [x for x in range(n) if len(g[x]) < 2], []  # alternating queues

        while True:
            for x in q:
                for y in g[x]:
                    g[y].remove(x)
                    if len(g[y]) == 1:
                        nq.append(y)
            if not nq:
                break  # skips alternate queues
            nq, q = [], nq
        return q

    def print_ans(self, ans):
        print(ans)

    def test(self):
        n = 6
        edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
        ans = self.findMinHeightTrees(n, edges)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
