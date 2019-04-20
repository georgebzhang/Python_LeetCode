class Solution(object):
    def exist(self, board, word):
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def neighbors(i0, j0):
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < N and 0 <= j < M:
                    result.append((i, j))
            return result

        def dfs(i, j, rem):
            if board[j][i] != rem[0]:
                return
            if (i, j) in visited:
                return
            visited.add((i, j))

            rem = rem[1:]
            if not rem:
                self.found = True
                return

            for n in neighbors(i, j):
                dfs(*n, rem)

            visited.remove((i, j))

        M, N = len(board), len(board[0])
        self.found = False
        for j in range(M):
            for i in range(N):
                visited = set()
                dfs(i, j, word)

        return self.found

    def print_grid(self, image):
        for row in image:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCESEEEFS"
        self.print_grid(board)
        print()
        ans = self.exist(board, word)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
