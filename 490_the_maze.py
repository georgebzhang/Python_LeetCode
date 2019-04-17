class Solution(object):
    # i represents rows (or y), j represents columns (or x)
    def hasPath(self, maze, start, destination):
        def ends(p):
            i, j = p
            result = []
            u, d, l, r = i-1, i+1, j-1, j+1
            while u >= 0 and maze[u][j] == 0:
                u -= 1
            result.append([u+1, j])
            while d < len(maze) and maze[d][j] == 0:
                d += 1
            result.append([d-1, j])
            while l >= 0 and maze[i][l] == 0:
                l -= 1
            result.append([i, l+1])
            while r < len(maze[0]) and maze[i][r] == 0:
                r += 1
            result.append([i, r-1])
            return result

        def dfs(p):
            if self.result:
                return
            i, j = p
            if visited[i][j]:
                return
            visited[i][j] = 1
            i_dest, j_dest = destination
            if i == i_dest and j == j_dest:
                self.result = True

            for e in ends(p):
                dfs(e)

        visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.result = False
        dfs(start)
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
