class Solution(object):
    def test_init(self):
        print('set(): ', end='')
        s = set()
        s.add(1)
        s.add(5)
        s.add(3)
        s.add(4)
        s.add(2)
        print(s)

    def test_init_iterable(self):
        print('set(iterable): ', end='')
        l = [1, 5, 3, 4, 2, 3, 3]
        s = set(l)
        print(s)

    def test_and(self):
        print('&: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1 & s2
        print(s)

    def test_contains(self):
        print('in: ', end='')
        s = {1, 2, 3, 4, 5}
        print(3 in s)

    def test_eq(self):
        print('==: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {2, 4, 1, 5, 3}
        print(s1 == s2)

    def test_ge(self):
        print('>=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {1, 2, 3}
        print(s1 >= s2)

    def test_getattribute(self):
        pass

    def test_gt(self):
        print('>: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {1, 2, 3}
        print(s1 > s2)

    def test_iand(self):
        print('&=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1 &= s2
        print(s1)

    def test_ior(self):
        print('|=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1 |= s2
        print(s1)

    def test_isub(self):
        print('-=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1 -= s2
        print(s1)

    def test_iter(self):
        print('iter: ', end='')
        s = {2, 5, 3, 1, 4}
        i = iter(s)
        print(next(i), next(i), next(i))

    def test_ixor(self):
        print('^=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1 ^= s2
        print(s1)

    def test_le(self):
        print('<=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {1, 2, 3, 4, 5, 6}
        print(s1 <= s2)

    def test_len(self):
        print('len: ', end='')
        s = {1, 2, 3, 4, 5}
        print(len(s))

    def test_lt(self):
        print('<: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {1, 2, 3, 4, 5, 6}
        print(s1 < s2)

    def test_ne(self):
        print('!=: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {1, 2, 3, 4, 5, 6}
        print(s1 != s2)

    def test_or(self):
        print('|: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1 | s2
        print(s)

    def test_rand(self):
        pass

    def test_reduce(self):
        pass

    def test_repr(self):
        print('repr: ', end='')
        s = {1, 2, 3, 4, 5}
        print(repr(s))

    def test_ror(self):
        pass

    def test_rsub(self):
        pass

    def test_rxor(self):
        pass

    def test_sizeof(self):
        pass

    def test_sub(self):
        print('-: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1 - s2
        print(s)

    def test_xor(self):
        print('^: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1 ^ s2
        print(s)

    def test_add(self):
        print('add: ', end='')
        s = {1, 2, 3, 4, 5}
        s.add(6)
        print(s)

    def test_clear(self):
        print('clear: ', end='')
        s = {1, 2, 3, 4, 5}
        s.clear()
        print(s)

    def test_copy(self):
        print('copy: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = s1.copy()
        print(s2)

    def test_difference(self):
        print('difference: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1.difference(s2)
        print(s)

    def test_difference_update(self):
        print('difference_update: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1.difference_update(s2)
        print(s1)

    def test_discard(self):
        print('discard: ', end='')
        s = {1, 2, 3, 4, 5}
        s.discard(6)
        s.discard(3)
        print(s)

    def test_intersection(self):
        print('intersection: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1.intersection(s2)
        print(s)

    def test_intersection_update(self):
        print('intersection_update: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1.intersection_update(s2)
        print(s1)

    def test_isdisjoint(self):
        print('isdisjoint: ', end='')
        s1 = {1, 2, 3}
        s2 = {4, 5, 6}
        print(s1.isdisjoint(s2))

    def test_issubset(self):
        print('issubset: ', end='')
        s1 = {1, 2, 3}
        s2 = {0, 1, 2, 3, 4}
        print(s1.issubset(s2))

    def test_issuperset(self):
        print('issuperset: ', end='')
        s1 = {0, 1, 2, 3, 4}
        s2 = {1, 2, 3}
        print(s1.issuperset(s2))

    def test_pop(self):
        print('pop: ', end='')
        s = {1, 2, 3, 4, 5}
        print(s.pop(), s)

    def test_remove(self):
        print('remove: ', end='')
        s = {1, 2, 3, 4, 5}
        s.remove(3)
        print(s)

    def test_symmetric_difference(self):
        print('symmetric_difference: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1.symmetric_difference(s2)
        print(s)

    def test_union(self):
        print('union: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s = s1.union(s2)
        print(s)

    def test_update(self):
        print('update: ', end='')
        s1 = {1, 2, 3, 4, 5}
        s2 = {3, 4, 5, 6, 7}
        s1.update(s2)
        print(s1)

    def test_set(self):
        self.test_init()
        self.test_init_iterable()
        self.test_and()
        self.test_contains()
        self.test_eq()
        self.test_ge()
        self.test_gt()
        self.test_iand()
        self.test_ior()
        self.test_isub()
        self.test_iter()
        self.test_ixor()
        self.test_le()
        self.test_len()
        self.test_lt()
        self.test_ne()
        self.test_or()
        self.test_repr()
        self.test_sub()
        self.test_xor()
        self.test_add()
        self.test_clear()
        self.test_copy()
        self.test_difference()
        self.test_difference_update()
        self.test_discard()
        self.test_intersection()
        self.test_intersection_update()
        self.test_isdisjoint()
        self.test_issubset()
        self.test_issuperset()
        self.test_pop()
        self.test_remove()
        self.test_symmetric_difference()
        self.test_union()
        self.test_update()


if __name__ == '__main__':
    s = Solution()
    s.test_set()
