class Solution(object):
    def minPathSum(self, grid):
        M, N = len(grid), len(grid[0])

        dp = [[0 for _ in range(N)] for _ in range(M)]
        for j in range(M-1, -1, -1):
            for i in range(N-1, -1, -1):
                if i == N-1 and j != M-1:
                    dp[j][i] = grid[j][i] + dp[j+1][i]
                elif j == M-1 and i != N-1:
                    dp[j][i] = grid[j][i] + dp[j][i+1]
                elif j != M-1 and i != N-1:
                    dp[j][i] = grid[j][i] + min(dp[j+1][i], dp[j][i+1])
                else:  # end
                    dp[j][i] = grid[j][i]

        return dp[0][0]

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
