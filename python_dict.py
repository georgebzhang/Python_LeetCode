class Solution(object):
    def test_fromkeys(self):
        print('fromkeys: ', end='')
        kset = {'Bob', 'Alice', 'George', 'Jane', 'Xavier'}
        value = 0
        d = dict.fromkeys(kset, value)
        print(d)

    def test_init(self):
        print('dict(): ', end='')
        d = dict()
        d['Bob'] = 5
        d['Alice'] = 8
        d['George'] = 69
        print(d)


    def test_init_mapping(self):
        print('dict(mapping): ', end='')
        mapping = {
            'Bob': 5,
            'Alice': 8,
            'George': 69,
            'Jane': 3,
            'Xavier': 1
        }
        d = dict(mapping)
        print(d)

    def test_init_iterable(self):
        print('dict(iterable): ', end='')
        l1 = ['Bob', 'Alice', 'George', 'Jane', 'Xavier']
        l2 = [5, 8, 69, 3, 1]
        # d = dict(zip(iter(l1), iter(l2)))  # iter() not necessary
        d = dict(zip(l1, l2))
        print(d)

    def test_init_iterable2(self):
        print('dict(iterable): ', end='')
        l = [('Bob', 5), ('George', 69), ('Alice', 8), ('Jane', 3), ('Xavier', 1)]  # can have pairs in lists, but tuples are faster
        d = dict(l)
        print(d)

    def test_init_1by1(self):
        print('dict[] =: ', end='')
        d = {}
        d['Bob'] = 5
        d['Alice'] = 8
        d['George'] = 69
        d['Jane'] = 3
        d['Xavier'] = 1
        print(d)

    def test_contains(self):
        print('in: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print('Alice' in d)

    def test_delitem(self):
        print('del: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        del d['Alice']
        print(d)

    def test_eq(self):
        print('==: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d1 = dict(mapping)
        l = [('Bob', 5), ('George', 69), ('Alice', 8), ('Jane', 3), ('Xavier', 1)]  # k, v pairs don't have to be inserted in same order
        d2 = dict(l)
        print(d1 == d2)

    def test_ge(self):
        pass

    def test_getattribute(self):
        pass

    def test_getitem(self):
        print('[]: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print(d['George'])

    def test_gt(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        i = iter(d)
        print(next(i), next(i), next(i))

    def test_le(self):
        pass

    def test_len(self):
        print('len: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print(len(d))

    def test_lt(self):
        pass

    def test_ne(self):
        print('!=: ', end='')
        mapping = {'Bob': 5, 'Alice': 7, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d1 = dict(mapping)
        l = [('Bob', 5), ('George', 69), ('Alice', 8), ('Jane', 3), ('Xavier', 1)]  # can have pairs in lists, but tuples are faster
        d2 = dict(l)
        print(d1 != d2)

    def test_reduce(self):
        pass

    def test_repr(self):
        print('repr: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print(repr(d))

    def test_setitem(self):
        print('[] =: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        d['George'] = 7
        d['New'] = 42
        print(d)

    def test_sizeof(self):
        pass

    def test_clear(self):
        print('clear: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        d.clear()
        print(d)

    def test_copy(self):
        print('copy: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d1 = dict(mapping)
        d2 = d1.copy()
        print(d2)

    def test_get(self):
        print('get: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print(d.get('Jane'))

    def test_items(self):
        print('items: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        for k, v in d.items():
            print(k, v, ' ', end='')
        print()

    def test_keys(self):
        print('keys: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        for k in d.keys():
            print(k, ' ', end='')
        print()

    def test_pop(self):
        print('pop: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print(d.pop('Alice'), d)

    def test_popitem(self):
        print('popitem: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        print(d.popitem(), d.popitem(), d)

    def test_setdefault(self):
        print('setdefault: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        d.setdefault('Newguy', 0)  # if 'Newguy' is not in dict, then add ('Newguy', default_value) to dict
        d.setdefault('Bob', 0)
        print(d)

    def test_update(self):
        print('update: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        d1 = {'Jane': 12}
        d.update(d1)
        print(d)

    def test_values(self):
        print('values: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        d = dict(mapping)
        for v in d.values():
            print(v, ' ', end='')
        print()

    def test_dict(self):
        self.test_fromkeys()
        self.test_init()
        self.test_init_mapping()
        self.test_init_iterable()
        self.test_init_iterable2()
        self.test_init_1by1()
        self.test_contains()
        self.test_delitem()
        self.test_eq()
        self.test_getitem()
        self.test_iter()
        self.test_len()
        self.test_ne()
        self.test_repr()
        self.test_setitem()
        self.test_clear()
        self.test_copy()
        self.test_get()
        self.test_items()
        self.test_keys()
        self.test_pop()
        self.test_popitem()
        self.test_setdefault()
        self.test_update()
        self.test_values()


if __name__ == '__main__':
    s = Solution()
    s.test_dict()
