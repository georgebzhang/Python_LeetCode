from collections import Counter


class Solution(object):
    def test_fromkeys(self):
        pass

    def test_init_string(self):
        print('Counter(string): ', end='')
        s = 'George'
        c = Counter(s)
        print(c)

    def test_init_list(self):
        print('Counter(list): ', end='')
        l = [1, 2, 3, 2, 1]
        c = Counter(l)
        print(c)

    def test_add(self):
        print('+: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c = c1 + c2
        print(c)

    def test_and(self):
        print('&: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c = c1 & c2
        print(c)

    def test_delitem(self):
        print('del: ', end='')
        s = 'George'
        c = Counter(s)
        del c['e']
        print(c)

    def test_iadd(self):
        print('+=: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1 += c2
        print(c1)

    def test_iand(self):
        print('&=: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1 &= c2
        print(c1)

    def test_ior(self):
        print('|=: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1 |= c2
        print(c1)

    def test_isub(self):  # keeps only keys with positive counts
        print('-=: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1 -= c2
        print(c1)

    def test_missing(self):
        pass

    def test_neg(self):
        print('neg: ', end='')
        s1 = 'abbcc'
        s2 = 'abdd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1.subtract(c2)  # need to use .subtract(...) to get negative counts
        c1 = -c1
        print(c1)

    def test_or(self):
        print('|: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c = c1 | c2
        print(c)

    def test_pos(self):
        print('pos: ', end='')
        s1 = 'abbcc'
        s2 = 'abdd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1.subtract(c2)  # need to use .subtract(...) to get negative counts
        c1 = +c1
        print(c1)

    def test_reduce(self):
        pass

    def test_repr(self):
        print('repr: ', end='')
        l = [1, 2, 3, 2, 1]
        c = Counter(l)
        print(repr(c))

    def test_sub(self):
        print('-: ', end='')
        s1 = 'abbcc'
        s2 = 'abd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c = c1 - c2
        print(c)

    def test_copy(self):
        print('copy: ', end='')
        l = [1, 2, 3, 2, 1]
        c1 = Counter(l)
        c2 = c1.copy()
        print(c2)

    def test_elements(self):
        s = 'abcabcabc'
        c = Counter(s)
        print(''.join(sorted(c.elements())))

    def test_most_common(self):
        print('most_common: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print(c.most_common(3))

    def test_subtract(self):  # keys allowed to reach negative counts
        print('subtract: ', end='')
        s1 = 'abbcc'
        s2 = 'abdd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1.subtract(c2)
        print(c1)

    def test_update(self):
        print('update: ', end='')
        s1 = 'abbcc'
        s2 = 'abdd'
        c1 = Counter(s1)
        c2 = Counter(s2)
        c1.update(c2)
        print(c1)

    def test_contains(self):
        print('contains: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print('b' in c)

    def test_eq(self):
        print('==: ', end='')
        s1 = 'abbcc'
        s2 = 'abbcc'
        c1 = Counter(s1)
        c2 = Counter(s2)
        print(c1 == c2)

    def test_ge(self):
        pass

    def test_getattribute(self):
        pass

    def test_getitem(self):
        print('[]: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print(c['b'])

    def test_gt(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        s = 'abcaba'
        c = Counter(s)
        i = iter(c)
        print(next(i), next(i), next(i))

    def test_le(self):
        pass

    def test_len(self):
        print('len: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print(len(c))

    def test_lt(self):
        pass

    def test_ne(self):
        print('!=: ', end='')
        s1 = 'abbcc'
        s2 = 'abbcc'
        c1 = Counter(s1)
        c2 = Counter(s2)
        print(c1 != c2)

    def test_setitem(self):
        print('[] =: ', end='')
        s = 'abcaba'
        c = Counter(s)
        c['b'] = 69
        print(c)

    def test_sizeof(self):
        pass

    def test_clear(self):
        print('clear: ', end='')
        s = 'abcaba'
        c = Counter(s)
        c.clear()
        print(c)

    def test_get(self):
        print('get: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print(c.get('d'), c.get('b'))

    def test_items(self):
        print('items: ', end='')
        s = 'abcaba'
        c = Counter(s)
        for k, v in c.items():
            print(k, v, ' ', end='')
        print()

    def test_keys(self):
        print('keys: ', end='')
        s = 'abcaba'
        c = Counter(s)
        for k in c.keys():
            print(k, ' ', end='')
        print()

    def test_pop(self):
        print('pop: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print(c.pop('b'), c)

    def test_popitem(self):
        print('popitem: ', end='')
        s = 'abcaba'
        c = Counter(s)
        print(c.popitem(), c)

    def test_setdefault(self):
        print('popitem: ', end='')
        s = 'abcaba'
        c = Counter(s)
        c.setdefault('d', 69)
        print(c)

    def test_values(self):
        print('values: ', end='')
        s = 'abcaba'
        c = Counter(s)
        for v in c.values():
            print(v, ' ', end='')
        print()

    def test_Counter(self):
        self.test_init_string()
        self.test_init_list()
        self.test_add()
        self.test_and()
        self.test_delitem()
        self.test_iadd()
        self.test_iand()
        self.test_ior()
        self.test_isub()
        self.test_neg()
        self.test_or()
        self.test_pos()
        self.test_repr()
        self.test_sub()
        self.test_copy()
        self.test_elements()
        self.test_most_common()
        self.test_subtract()
        self.test_update()
        self.test_contains()
        self.test_eq()
        self.test_getitem()
        self.test_iter()
        self.test_len()
        self.test_ne()
        self.test_setitem()
        self.test_clear()
        self.test_get()
        self.test_items()
        self.test_keys()
        self.test_pop()
        self.test_popitem()
        self.test_setdefault()
        self.test_values()


if __name__ == '__main__':
    s = Solution()
    s.test_Counter()
