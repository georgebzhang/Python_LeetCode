class Solution(object):
    def numIslands(self, grid):
        def neighbors(p):
            i, j = p
            neighbors = []
            if i-1 >= 0:
                neighbors.append((i-1, j))
            if i+1 < len(grid[0]):
                neighbors.append((i+1, j))
            if j-1 >= 0:
                neighbors.append((i, j-1))
            if j+1 < len(grid):
                neighbors.append((i, j+1))
            return neighbors

        def dfs(p):
            i, j = p
            if grid[j][i] != '1':
                return
            if p in visited:
                return
            visited.add(p)
            island.append(p)
            for n in neighbors(p):
                dfs(n)

        visited = set()
        islands = []
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                p = (i, j)
                if grid[j][i] == '1' and p not in visited:
                    island = []
                    dfs(p)
                    islands.append(island)

        return len(islands)

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
