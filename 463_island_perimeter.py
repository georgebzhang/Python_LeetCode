class Solution(object):
    def islandPerimeter(self, grid):
        def neighbors(p):
            neighbors = []
            i, j = p
            if i-1 >= 0:
                neighbors.append((i-1, j))
            if i+1 < dims_grid[1]:
                neighbors.append((i+1, j))
            if j-1 >= 0:
                neighbors.append((i, j-1))
            if j+1 < dims_grid[0]:
                neighbors.append((i, j+1))
            return neighbors

        def dfs(p):
            if p in visited:
                return
            visited.add(p)
            i, j = p
            if grid[j][i] != 1:
                return
            lands.append(p)
            for n in neighbors(p):
                dfs(p)

        visited = set()
        lands = []
        dims_grid = [len(grid), len(grid[0])]
        for j in range(dims_grid[0]):
            for i in range(dims_grid[1]):
                if grid[j][i] == 1:
                    p = (i, j)
                    dfs(p)

        def perimeter(p):
            perimeter = 0
            i, j = p
            perimeter += 1 if i-1 < 0 or grid[j][i-1] == 0 else 0
            perimeter += 1 if i+1 >= dims_grid[1] or grid[j][i+1] == 0 else 0
            perimeter += 1 if j-1 < 0 or grid[j-1][i] == 0 else 0
            perimeter += 1 if j+1 >= dims_grid[0] or grid[j+1][i] == 0 else 0
            return perimeter

        result = 0
        for p in lands:
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
