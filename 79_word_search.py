class Solution(object):
    def exist(self, board, word):
        def neighbors(p):
            result = []
            i, j = p
            if i-1 >= 0:
                result.append((i-1, j))
            if i+1 < len(board[0]):
                result.append((i+1, j))
            if j-1 >= 0:
                result.append((i, j-1))
            if j+1 < len(board):
                result.append((i, j+1))
            return result

        def dfs(p, s):
            if self.result:
                return
            if p in visited:
                return
            i, j = p
            if board[j][i] != s[0]:
                return

            visited.add(p)

            s = s[1:]
            if not s:
                self.result = True
                return

            for n in neighbors(p):
                dfs(n, s)

            visited.remove(p)

        self.result = False
        for j in range(len(board)):
            for i in range(len(board[0])):
                visited = set()
                dfs((i, j), word)

        return self.result

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
