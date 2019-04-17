from collections import deque


class Solution(object):
    # i represents rows (or y), j represents columns (or x)
    def hasPath(self, maze, start, destination):
        def ends(p):
            i, j = p
            result = []
            u, d, l, r = i-1, i+1, j-1, j+1
            while u >= 0 and maze[u][j] == 0:  # up
                u -= 1
            if u+1 != i:  # appending (i, j) results in duplicate work
                result.append((u+1, j))

            while d < len(maze) and maze[d][j] == 0:  # down
                d += 1
            if d-1 != i:
                result.append((d-1, j))

            while l >= 0 and maze[i][l] == 0:  # left
                l -= 1
            if l+1 != j:
                result.append((i, l+1))

            while r < len(maze[0]) and maze[i][r] == 0:  # right
                r += 1
            if r-1 != j:
                result.append((i, r-1))

            return result

        def bfs(p):
            q = deque([p])
            while q:
                p = q.popleft()
                if self.result:
                    continue
                if p in visited:
                    continue
                visited.add(p)
                i, j = p
                i_dest, j_dest = destination
                if i == i_dest and j == j_dest:
                    self.result = True
                q.extend(ends(p))

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
