class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        dirs = ((1, 0), (0, 1))
        def neighbors(p):
            i0, j0 = p
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < N and 0 <= j < M and obstacleGrid[j][i] != 1:
                    result.append((i, j))
            return result

        def paths(p):
            if p == end:
                return [[p]]
            result = []
            for n in neighbors(p):
                for path in paths(n):
                    result.append([p] + path)
            return result

        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[M-1][N-1] == 1:  # if start or end has obstacle
            return 0
        start, end = (0, 0), (N-1, M-1)
        return len(paths(start))

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
