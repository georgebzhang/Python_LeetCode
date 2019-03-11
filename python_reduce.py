from functools import reduce  # must import reduce


class Solution(object):
    def mult(self, num1, num2):  # helper function for test_fn_mult()
        return num1 * num2

    def test_fn_mult(self):
        print('map(function, list): ', end='')
        l = [1, 2, 3, 4, 5]
        m = reduce(self.mult, l)
        print(m)

    def test_lambda_mult(self):
        print('map(lambda, list): ', end='')
        l = [1, 2, 3, 4, 5]
        m = reduce(lambda num1, num2: num1 * num2, l)
        print(m)

    def test_reduce(self):
        self.test_fn_mult()
        self.test_lambda_mult()


if __name__ == '__main__':
    s = Solution()
    s.test_reduce()
