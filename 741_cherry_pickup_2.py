import sys


class Solution(object):
    def cherryPickup(self, grid):
        dirs = ((1, 0, 0), (0, 1, 0), (1, 0, 1), (0, 1, 1))  # (di1, dj1, di2)
        def neighbors(i10, j10, i20):
            result = []
            for di1, dj1, di2 in dirs:
                i1, j1, i2 = i10+di1, j10+dj1, i20+di2
                j2 = i1 + j1 - i2
                if 0 <= i1 < N and 0 <= j1 < M and 0 <= i2 < N and 0 <= j2 < M and grid[j1][i1] != -1 and grid[j2][i2] != -1:
                    result.append((i1, j1, i2))
            return result

        def dfs(i1, j1, i2):
            j2 = i1 + j1 - i2
            dp[i2][j1][i1] = grid[j1][i1]
            if (i1, j1) != (i2, j2):
                dp[i2][j1][i1] += grid[j2][i2]
            else:
                if (i1, j1) == end:
                    return
            ns = neighbors(i1, j1, i2)
            for i12, j12, i22 in ns:
                dfs(i12, j12, i22)
            n_dp = [dp[i22][j12][i12] for i12, j12, i22 in ns]
            dp[i2][j1][i1] += -sys.maxsize if not n_dp else max(n_dp)

        M, N = len(grid), len(grid[0])
        end = (N-1, M-1)
        # dp[i2][j1][i1], i1 + j1 = i2 + j2 = M+N-2
        dp = [[[0 for _ in range(N)] for _ in range(M)] for _ in range(N)]

        dfs(0, 0, 0)
        return max(0, dp[0][0][0])

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
        grid = [
            [1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1]
        ]
        self.print_grid(grid)
        print()
        ans = self.cherryPickup(grid)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
