class Solution(object):
    def is_alnum(self, char):  # helper function for test_fn_isalnum()
        return char.isalnum()

    def test_fn_isalnum(self):
        print('map(function, list): ', end='')
        s = 'Hel? L!$@o Im 2*7'
        m = list(filter(self.is_alnum, s))
        print(''.join(m))

    def test_lambda_isalnum(self):
        print('map(lambda, list): ', end='')
        s = 'Hel? L!$@o Im 2*7'
        m = list(filter(lambda char: char.isalnum(), s))
        print(''.join(m))

    def test_filter(self):
        self.test_fn_isalnum()
        self.test_lambda_isalnum()


if __name__ == '__main__':
    s = Solution()
    s.test_filter()
