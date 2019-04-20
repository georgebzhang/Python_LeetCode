class Solution(object):
    def cherryPickup(self, grid):
        M, N = len(grid), len(grid[0])
        T = M+N-1  # total time or number of steps
        end = (N-1, M-1)
        # dp[t][p][i]
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[0][0] = grid[0][0]

        for t in range(1, T):
            for i in range(N-1, -1, -1):
                for p in range(N-1, -1, -1):
                    j, q = t-i, t-p
                    if j < 0 or j >= M or q < 0 or q >= M or grid[j][i] < 0 or grid[q][p] < 0:
                        dp[p][i] = -1
                        continue

                    if i > 0:
                        dp[p][i] = max(dp[p][i], dp[p][i-1])
                    if p > 0:
                        dp[p][i] = max(dp[p][i], dp[p-1][i])
                    if i > 0 and p > 0:
                        dp[p][i] = max(dp[p][i], dp[p-1][i-1])
                    if dp[p][i] >= 0:
                        dp[p][i] += grid[j][i]
                        if i != p:
                            dp[p][i] += grid[q][p]

        return max(0, dp[N-1][N-1])

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
