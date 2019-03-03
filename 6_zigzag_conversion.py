class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:  # base case
            return s

        data = [''] * numRows

        row = 0
        d_row = 0  # change in row

        for i in range(len(s)):
            data[row] += s[i]
            if row == 0:
                d = 1
            if row == numRows - 1:
                d = -1
            row += d

        result = ''
        for row in range(numRows):
            result += data[row]

        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        s = 'PAYPALISHIRING'
        numRows = 4
        ans = self.convert(s, numRows)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
