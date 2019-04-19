import sys


class Solution(object):
    def minPathSum(self, grid):
        dirs = ((1, 0), (0, 1))
        def neighbors(p):
            i0, j0 = p
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < N and 0 <= j < M:
                    result.append((i, j))
            return result

        def paths(p):
            if p == end:
                return [[end]]

            result = []
            for n in neighbors(p):
                for path in paths(n):
                    result.append([p] + path)
            return result

        M, N = len(grid), len(grid[0])
        start, end = (0, 0), (N-1, M-1)

        result = sys.maxsize
        for path in paths(start):
            result = min(result, sum([grid[j][i] for i, j in path]))

        return result

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
        self.print_grid(grid)
        print()
        ans = self.minPathSum(grid)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
