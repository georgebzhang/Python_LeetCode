class Solution(object):
    def findWords(self, board, words):
        def neighbors(p):
            i, j = p
            result = []
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
            if self.found:
                return
            if p in visited:
                return
            i, j = p
            if board[j][i] != s[0]:
                return
            visited.add(p)

            s = s[1:]
            if not s:
                self.found = True
                return

            for n in neighbors(p):
                dfs(n, s)

            visited.remove(p)

        result = []
        for word in words:
            self.found = False
            for j in range(len(board)):
                for i in range(len(board[0])):
                    visited = set()
                    dfs((i, j), word)
            if self.found:
                result.append(word)

        return result

    def print_grid(self, image):
        for row in image:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        self.print_grid(board)
        print()
        ans = self.findWords(board, words)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
