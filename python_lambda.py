class Solution(object):
    def test_fn_double(self):
        print('double: ', end='')
        double = lambda x: 2 * x
        print(double(3))

    def test_fn_max(self):
        print('max: ', end='')
        max = lambda x, y: x if x > y else y
        print(max(5, 8))

    def test_lambda(self):
        self.test_fn_double()
        self.test_fn_max()


if __name__ == '__main__':
    s = Solution()
    s.test_lambda()
