class Solution:
    def rotate(self, matrix):
        N = len(matrix)
        for j in range(N):
            for i in range(j, N):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for row in matrix:
            row.reverse()

    def print_grid(self, grid):
        for row in grid:
            print(row)

    def print_ans(self, ans):
        self.print_grid(ans)

    def test(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.print_grid(matrix)
        print()
        self.rotate(matrix)
        self.print_ans(matrix)


if __name__ == '__main__':
    s = Solution()
    s.test()
