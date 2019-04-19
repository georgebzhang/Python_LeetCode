class Solution(object):
    def hasPath(self, maze, start, destination):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def ends(i0, j0):
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                while 0 <= i < N and 0 <= j < M and maze[j][i] != 1:
                    i += di
                    j += dj
                i -= di
                j -= dj
                if (i, j) != (i0, j0):
                    result.append((i, j))

            return result

        def dfs(i, j):
            if self.result:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            if (i, j) == dest:
                self.result = True
            for i2, j2 in ends(i, j):
                dfs(i2, j2)

        M, N = len(maze), len(maze[0])
        start.reverse()
        destination.reverse()
        start, dest = tuple(start), tuple(destination)

        self.result = False
        visited = set()
        dfs(*start)  # unpack tuple
        return self.result

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
