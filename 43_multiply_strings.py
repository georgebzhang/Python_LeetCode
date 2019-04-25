class Solution:
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))

    def print_answer(self, ans):
        print(ans)

    def test(self):
        num1, num2 = '2', '3'
        ans = self.multiply(num1, num2)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
