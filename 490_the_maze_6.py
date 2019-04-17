from collections import deque


class Solution(object):
    # i represents rows (or y), j represents columns (or x)
    def hasPath(self, maze, start, destination):
        def ends(p):  # slower but cleaner code
            i0, j0 = p
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                while 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0:
                    i += di
                    j += dj
                i -= di
                j -= dj
                if i != i0 or j != j0:
                    result.append((i, j))

            return result

        def bfs(p):
            q = deque([p])
            while q:
                p = q.popleft()
                if self.result:
                    return
                if p in visited:
                    continue
                visited.add(p)
                i, j = p
                i_dest, j_dest = destination
                if i == i_dest and j == j_dest:
                    self.result = True
                q.extend(ends(p))

        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        visited = set()
        self.result = False
        bfs(tuple(start))
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
