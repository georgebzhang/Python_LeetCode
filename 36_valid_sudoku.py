class Solution(object):
    def isValidSudoku(self, board):
        N = 9
        rows = [set() for _ in range(N)]
        columns = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for j in range(N):
            for i in range(N):
                val = board[j][i]
                if val != '.':
                    box_num = (j // 3) * 3 + i // 3
                    if val in rows[j] or val in columns[i] or val in boxes[box_num]:
                        return False
                    rows[j].add(val)
                    columns[i].add(val)
                    boxes[box_num].add(val)

        return True

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
        self.print_grid(board)
        print()
        ans = self.isValidSudoku(board)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
