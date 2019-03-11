class Solution(object):
    def square(self, num):  # helper function for test_fn_square()
        return num ** 2

    def test_fn_square(self):
        print('map(function, list): ', end='')
        l = [1, 2, 3, 4, 5]
        m = list(map(self.square, l))
        print(m)

    def test_lambda_square(self):
        print('map(lambda, list): ', end='')
        l = [1, 2, 3, 4, 5]
        m = list(map(lambda x: x ** 2, l))
        print(m)

    def upper(self, char):
        return char.upper()

    def test_fn_upper(self):
        print('map(function, list): ', end='')
        s = 'George'
        m = list(map(self.upper, s))
        print(''.join(m))

    def test_lambda_upper(self):
        print('map(lambda, list): ', end='')
        s = 'George'
        m = list(map(lambda char: char.upper(), s))
        print(''.join(m))

    def strip_not_alnum(self, char):  # helper function for test_fn_strip_not_alnum()
        return char if char.isalnum() else ''

    def test_fn_strip_not_alnum(self):
        print('map(function, list): ', end='')
        s = 'Hel? L!$@o Im 2*7'
        m = list(map(self.strip_not_alnum, s))
        print(''.join(m))

    def test_lambda_strip_not_alnum(self):
        print('map(lambda, list): ', end='')
        s = 'Hel? L!$@o Im 2*7'
        m = list(map(lambda char: char if char.isalnum() else '', s))
        print(''.join(m))

    def test_map(self):
        self.test_fn_square()
        self.test_lambda_square()
        self.test_fn_upper()
        self.test_lambda_upper()
        # Stripping non alphanumeric characters is better suited to FILTER
        self.test_fn_strip_not_alnum()
        self.test_lambda_strip_not_alnum()

if __name__ == '__main__':
    s = Solution()
    s.test_map()
