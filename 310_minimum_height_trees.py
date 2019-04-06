import sys
from collections import defaultdict


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        def max_height(v):
            if v in visited:
                return 0
            visited.add(v)
            n_heights = []
            for n in g[v]:  # for neighbor of vertex
                n_heights.append(max_height(n))
            return max(n_heights)+1

        if n == 1:
            return [0]

        g = defaultdict(list)
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        visited = set()
        v_heights = {}
        min_height = sys.maxsize
        for v in g:  # for vertex in graph
            h = max_height(v)
            v_heights[v] = h
            min_height = min(min_height, h)
            visited.clear()

        result = []
        for v in g:
            if v_heights[v] == min_height:
                result.append(v)

        return result

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
