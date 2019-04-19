import sys


class Solution(object):
    # incorrect greedy method
    def cherryPickup(self, grid):
        dirs = ((1, 0), (0, 1))
        def neighbors(i0, j0):
            result = []
            for dir in dirs:
                di, dj = dir
                i, j = i0 + di, j0 + dj
                if 0 <= i < len(grid[0]) and 0 <= j < len(grid) and grid[j][i] != -1:
                    result.append((i, j))
            return result

        def best_path():
            dp = [[0 for _ in range(M)] for _ in range(N)]
            for j in range(M-1, -1, -1):
                for i in range(N-1, -1, -1):
                    if grid[j][i] == -1:
                        continue
                    dp[j][i] = grid[j][i]
                    if (i, j) != end:
                        n_dp = [dp[j2][i2] for i2, j2 in neighbors(i, j)]
                        dp[j][i] += -sys.maxsize if not n_dp else max(n_dp)

            if dp[0][0] < 0:
                return None

            i, j = 0, 0
            result = []
            while True:
                result.append((i, j))
                if (i, j) == end:
                    break
                temp = -sys.maxsize
                for i2, j2 in neighbors(i, j):
                    if dp[j2][i2] > temp:
                        temp = dp[j2][i2]
                        i, j = i2, j2

            return result

        M, N = len(grid), len(grid[0])
        start, end = (0, 0), (N-1, M-1)

        result = 0
        path = best_path()  # forward path
        if not path:
            return 0

        for i, j in path:
            result += grid[j][i]
            grid[j][i] = 0  # remove cherry

        for i, j in best_path():  # backward path
            result += grid[j][i]

        return result

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        # grid = [[1, 1, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]
        grid = [
            [1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1]
        ]
        self.print_grid(grid)
        print()
        ans = self.cherryPickup(grid)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
