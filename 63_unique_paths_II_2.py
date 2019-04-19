class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:  # if start or end has obstacle
            return 0
        dp = [[0 for _ in range(N)] for _ in range(M)]
        dp[0][0] = 1

        # Python does some casting for us
        for j in range(1, M):
            dp[j][0] = obstacleGrid[j][0] == 0 and dp[j-1][0]

        for i in range(1, N):
            dp[0][i] = obstacleGrid[0][i] == 0 and dp[0][i-1]

        for j in range(1, M):
            for i in range(1, N):
                dp[j][i] = 0 if obstacleGrid[j][i] else dp[j-1][i] + dp[j][i-1]

        return dp[M-1][N-1]

    def print_ans(self, ans):
        print(ans)

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def test(self):
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.print_grid(obstacleGrid)
        print()
        ans = self.uniquePathsWithObstacles(obstacleGrid)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
