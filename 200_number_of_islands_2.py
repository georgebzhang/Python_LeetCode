class Solution(object):
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid[0]) and 0 <= j < len(grid) and grid[j][i] == '1':
                grid[j][i] = '0'
                [sink(i, j) for i, j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]]
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid[0])) for j in range(len(grid))) if grid else 0

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
