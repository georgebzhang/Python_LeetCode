from collections import deque
import sys


class Solution(object):
    def hasPath(self, maze, start, destination):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def ends(i0, j0):
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                dist = 0
                while 0 <= i < N and 0 <= j < M and maze[j][i] != 1:
                    i += di
                    j += dj
                    dist += 1
                i -= di
                j -= dj
                if (i, j) != (i0, j0):
                    if dp[j0][i0]+dist < dp[j][i]:
                        dp[j][i] = dp[j0][i0]+dist
                        result.append((i, j))

            return result

        def bfs(i, j):
            q = deque([(i, j)])
            while q:
                i, j = q.popleft()
                q.extend(ends(i, j))

        M, N = len(maze), len(maze[0])
        start.reverse()
        destination.reverse()
        start, dest = tuple(start), tuple(destination)
        i_s, j_s = start
        i_d, j_d = dest

        dp = [[sys.maxsize for _ in range(N)] for _ in range(M)]
        dp[j_s][i_s] = 0
        bfs(*start)  # unpack tuple
        return -1 if dp[j_d][i_d] == sys.maxsize else dp[j_d][i_d]

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
        start = [0, 4]
        destination = [4, 4]
        self.print_grid(maze)
        print()
        ans = self.hasPath(maze, start, destination)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
