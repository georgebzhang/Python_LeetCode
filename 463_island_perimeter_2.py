class Solution(object):
    def islandPerimeter(self, grid):
        def perimeter(p):
            i, j = p
            if grid[j][i] != 1:
                return 0
            perimeter = 0
            perimeter += 1 if i-1 < 0 or grid[j][i-1] == 0 else 0
            perimeter += 1 if i+1 >= len(grid[0]) or grid[j][i+1] == 0 else 0
            perimeter += 1 if j-1 < 0 or grid[j-1][i] == 0 else 0
            perimeter += 1 if j+1 >= len(grid) or grid[j+1][i] == 0 else 0
            return perimeter

        result = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                p = (i, j)
                result += perimeter(p)

        return result

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        self.print_grid(grid)
        ans = self.islandPerimeter(grid)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
