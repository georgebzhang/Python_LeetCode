class Solution(object):
    def gen_square(self, l):
        for num in l:
            yield num ** 2

    def test_fn_square(self):
        print('function: ', end='')
        l = [1, 2, 3, 4, 5]
        gen = self.gen_square(l)
        for i in gen:
            print(i, ' ', end='')
        print()

    def test_listcomp_square(self):
        print('list comp: ', end='')
        l = [1, 2, 3, 4, 5]
        gen = (num ** 2 for num in l)
        for i in gen:
            print(i, ' ', end='')
        print(type(gen))

    def test_generator(self):
        self.test_fn_square()
        self.test_listcomp_square()


if __name__ == '__main__':
    s = Solution()
    s.test_generator()
