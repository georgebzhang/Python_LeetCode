class Solution:
    def multiply(self, num1, num2):
        def str2int(s):
            result = 0
            for k in s:
                result = 10*result + ord(k)-ord('0')

            return result

        def int2str(i):
            digits = []
            while i > 0:
                digits.append(i % 10)
                i = i // 10

            digits.reverse()

            keys = '0123456789'
            result = ''
            for d in digits:
                result += keys[d]

            return result

        result = int2str(str2int(num1)*str2int(num2))

        return '0' if not result else result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        num1, num2 = '2', '3'
        ans = self.multiply(num1, num2)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
