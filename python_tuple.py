class Solution(object):
    def test_add(self):
        print('+: ', end='')
        t1 = (1, 2, 3)
        t2 = (4, 5, 6)
        print(t1 + t2)

    def test_contains(self):
        print('in: ', end='')
        t = (1, 2, 3, 4, 5)
        print(3 in t)

    def test_eq(self):
        print('==: ', end='')
        t1 = (1, 2, 3)
        t2 = (1, 2, 3)
        print(t1 == t2)


    def test_tuple(self):
        self.test_add()
        self.test_contains()
        self.test_eq()


if __name__ == '__main__':
    s = Solution()
    s.test_tuple()
