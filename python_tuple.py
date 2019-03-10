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

    def test_ge(self):
        print('>=: ', end='')
        t1 = (1, 2, 4)
        t2 = (1, 2, 3)
        print(t1 >= t2)

    def test_getattribute(self):
        pass

    def test_getitem(self):
        print('getitem: ', end='')
        t = (1, 2, 3, 4, 5)
        print(t[2])

    def test_gt(self):
        print('>: ', end='')
        t1 = (1, 2, 4)
        t2 = (1, 2, 3)
        print(t1 > t2)

    def test_hash(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        t = (1, 2, 3, 4, 5)
        i = iter(t)
        print(next(i), next(i), next(i))

    def test_le(self):
        print('<=: ', end='')
        t1 = (1, 2, 2)
        t2 = (1, 2, 3)
        print(t1 <= t2)

    def test_len(self):
        print('len: ', end='')
        t = (1, 2, 3, 4, 5)
        print(len(t))

    def test_lt(self):
        print('<: ', end='')
        t1 = (1, 2, 2)
        t2 = (1, 2, 3)
        print(t1 < t2)

    def test_mul(self):
        print('*: ', end='')
        t = (1, 2, 3)
        t = t * 3
        print(t)

    def test_ne(self):
        print('!=: ', end='')
        t1 = (1, 2, 2)
        t2 = (1, 2, 3)
        print(t1 != t2)

    def test_repr(self):
        print('repr: ', end='')
        t = (1, 2, 3, 4, 5)
        print(repr(t))

    def test_rmul(self):
        pass

    def test_count(self):
        print('count: ', end='')
        t = (1, 2, 3, 3, 2, 3)
        print(t.count(3))

    def test_index(self):
        print('index: ', end='')
        t = (1, 2, 3, 4, 5)
        print(t.index(3))


    def test_tuple(self):
        self.test_add()
        self.test_contains()
        self.test_eq()
        self.test_ge()
        self.test_getitem()
        self.test_gt()
        self.test_iter()
        self.test_le()
        self.test_len()
        self.test_lt()
        self.test_mul()
        self.test_ne()
        self.test_repr()
        self.test_count()
        self.test_index()


if __name__ == '__main__':
    s = Solution()
    s.test_tuple()
