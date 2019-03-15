class Solution(object):
    def test_abs(self):
        print('abs: ', end='')
        print(abs(-5))

    def test_all(self):
        print('all: ', end='')
        l = [1, 2, 3, 4, 5]
        print(all(num > 0 for num in l))

    def test_any(self):
        print('any: ', end='')
        l = [-1, 2, 3, 4, 5]
        print(any(num < 0 for num in l))

    def test_delattr(self):
        pass

    def test_divmod(self):
        print('divmod: ', end='')
        print(divmod(5, 3))

    def test_hasattr(self):
        pass

    def test_hash(self):
        print('hash: ', end='')
        print(hash('hi'))

    def test_help(self):
        print('help: ', end='')
        help(str)

    def test_hex(self):
        print('hex: ', end='')
        print(hex(69))

    def test_id(self):
        print('id: ', end='')
        n = 69
        print(id(n))

    def test_input(self):
        pass

    def test_isinstance(self):
        print('isinstance: ', end='')
        l = [1, 2, 3, 4, 5]
        print(isinstance(l, list))

    def test_issubclass(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        l = [1, 2, 3, 4, 5]
        i = iter(l)
        print(next(i), next(i), next(i))

    def test_len(self):
        print('iter: ', end='')
        l = [1, 2, 3, 4, 5]
        print(len(l))

    def test_max(self):
        print('max: ', end='')
        l = [1, 2, 3, 4, 5]
        print(max(l))

    def test_min(self):
        print('min: ', end='')
        l = [1, 2, 3, 4, 5]
        print(min(l))

    def test_next(self):
        pass

    def test_oct(self):
        print('oct: ', end='')
        print(oct(69))

    def test_open(self):
        pass

    def test_ord(self):
        print('ord: ', end='')
        ord_a = ord('a')
        z_ind = ord('z') - ord_a
        print(z_ind)

    def test_pow(self):
        print('pow: ', end='')
        print(pow(5, 3))

    def test_print(self):
        pass

    def test_repr(self):
        pass

    def test_round(self):
        print('round: ', end='')
        print(round(1.5))

    def test_setattr(self):
        pass

    def test_sorted(self):
        print('sorted: ', end='')
        l = [3, 5, 2, 1, 4]
        l = sorted(l)
        print(l)

    def test_sum(self):
        print('sum: ', end='')
        l = [1, 2, 3, 4, 5]
        print(sum(l))

    def test_builtins(self):
        self.test_abs()
        self.test_all()
        self.test_any()
        self.test_divmod()
        self.test_hash()
        # self.test_help()
        self.test_hex()
        self.test_id()
        self.test_isinstance()
        self.test_iter()
        self.test_len()
        self.test_max()
        self.test_min()
        self.test_oct()
        self.test_ord()
        self.test_pow()
        self.test_round()
        self.test_sorted()
        self.test_sum()


if __name__ == '__main__':
    s = Solution()
    s.test_builtins()
