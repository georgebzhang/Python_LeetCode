from collections import deque
import sys


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        dirs = ((1, 0), (0, 1))
        def neighbors(i0, j0):
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < N and 0 <= j < M:
                    result.append((i, j))
            return result

        M, N = len(dungeon), len(dungeon[0])
        end = (N-1, M-1)
        dp = [[0 for _ in range(N)] for _ in range(M)]
        dp[-1][-1] = max((-dungeon[-1][-1]+1), 1)

        for j in range(M)[::-1]:
            for i in range(N)[::-1]:
                if (i, j) == end:
                    continue
                n_dp = [dp[j2][i2] for i2, j2 in neighbors(i, j)]
                dp[j][i] = max(min(n_dp)-dungeon[j][i], 1)

        return dp[0][0]

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
        self.print_grid(dungeon)
        print()
        ans = self.calculateMinimumHP(dungeon)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
