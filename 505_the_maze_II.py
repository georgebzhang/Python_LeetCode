import sys


class Solution(object):
    # i represents rows (or y), j represents columns (or x)
    def hasPath(self, maze, start, destination):
        def ends(p):
            i0, j0 = p
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                dist = 0
                while 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0:
                    i += di
                    j += dj
                    dist += 1
                i -= di
                j -= dj

                if i != i0 or j != j0:
                    if dists[i0][j0]+dist < dists[i][j]:
                        dists[i][j] = dists[i0][j0]+dist
                        result.append((i, j))

            return result

        def dfs(p):
            i, j = p
            for e in ends(p):
                dfs(e)

        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        dists = [[sys.maxsize for _ in range(len(maze[0]))] for _ in range(len(maze))]
        i_start, j_start = start
        dists[i_start][j_start] = 0
        dfs(tuple(start))
        i_dest, j_dest = destination
        return -1 if dists[i_dest][j_dest] == sys.maxsize else dists[i_dest][j_dest]

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
