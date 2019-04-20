class Solution(object):
    def numIslands(self, grid):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def neighbors(i0, j0):
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 +dj
                if 0 <= i < N and 0 <= j < M and grid[j][i] == '1':
                    result.append((i, j))
            return result

        def sink(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            grid[j][i] = '0'
            for n in neighbors(i, j):
                sink(*n)

        if not grid:
            return 0

        M, N = len(grid), len(grid[0])
        visited = set()
        result = 0
        for j in range(M):
            for i in range(N):
                if grid[j][i] == '1':
                    result += 1
                    sink(i, j)

        return result

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
        self.print_grid(grid)
        ans = self.numIslands(grid)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
