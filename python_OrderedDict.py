from collections import OrderedDict


class Solution(object):
    def test_fromkeys(self):
        print('fromkeys: ', end='')
        kset = {'Bob', 'Alice', 'George', 'Jane', 'Xavier'}
        value = 0
        od = OrderedDict.fromkeys(kset, value)
        print(od)

    def test_init_mapping(self):
        print('OrderedDict(mapping): ', end='')
        mapping = {
            'Bob': 5,
            'Alice': 8,
            'George': 69,
            'Jane': 3,
            'Xavier': 1
        }
        od = OrderedDict(mapping)
        print(od)

    def test_init_iterable(self):
        print('OrderedDict(iterable): ', end='')
        l1 = ['Bob', 'Alice', 'George', 'Jane', 'Xavier']
        l2 = [5, 8, 69, 3, 1]
        od = OrderedDict(zip(l1, l2))
        print(od)

    def test_init_iterable2(self):
        print('OrderedDict(iterable): ', end='')
        l = [('Bob', 5), ('George', 69), ('Alice', 8), ('Jane', 3), ('Xavier', 1)]
        od = OrderedDict(l)
        print(od)

    def test_init(self):
        print('OrderedDict(): ', end='')
        od = OrderedDict()
        od['Bob'] = 5
        od['Alice'] = 8
        od['George'] = 69
        print(od)

    def test_contains(self):
        print('in: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print('Alice' in od)

    def test_delitem(self):
        print('del: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        del od['Alice']
        print(od)

    def test_eq(self):
        print('==: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od1 = OrderedDict(mapping)
        l = [('Bob', 5), ('Alice', 8), ('George', 69), ('Jane', 3), ('Xavier', 1)]  # items must be inserted in same order for OrderedDicts to be equal
        od2 = OrderedDict(l)
        print(od1 == od2)

    def test_ge(self):
        pass

    def test_getattribute(self):
        pass

    def test_getitem(self):
        print('[]: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print(od['George'])

    def test_gt(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        i = iter(od)
        print(next(i), next(i), next(i))

    def test_le(self):
        pass

    def test_len(self):
        print('[]: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print(len(od))

    def test_lt(self):
        pass

    def test_ne(self):
        print('!=: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od1 = OrderedDict(mapping)
        l = [('Bob', 5), ('Alice', 8), ('George', 69), ('Jane', 3), ('Xavier', 1)]
        od2 = OrderedDict(l)
        print(od1 != od2)

    def test_reduce(self):
        pass

    def test_repr(self):
        print('!=: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print(repr(od))

    def test_reversed(self):
        print('reversed: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        i = reversed(od)
        print(next(i), next(i), next(i))

    def test_setitem(self):
        print('[] =: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        od['George'] = 7
        od['New'] = 42
        print(od)

    def test_sizeof(self):
        pass

    def test_clear(self):
        print('clear: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        od.clear()
        print(od)

    def test_copy(self):
        print('copy: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od1 = OrderedDict(mapping)
        od2 = od1.copy()
        print(od2)

    def test_get(self):
        print('get: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print(od.get('Jane'))

    def test_items(self):
        print('items: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        for k, v in od.items():
            print(k, v, ' ', end='')
        print()

    def test_keys(self):
        print('keys: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        for k in od.keys():
            print(k, ' ', end='')
        print()

    def test_move_to_end(self):
        print('move_to_end: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        od.move_to_end('George', last=True)
        od.move_to_end('Jane', last=False)
        print(od)

    def test_pop(self):
        print('pop: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print(od.pop('Alice'), od)

    def test_popitem(self):
        print('popitem: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        print(od.popitem(last=True), od.popitem(last=False), od)

    def test_setdefault(self):
        print('setdefault: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        od.setdefault('Newguy', 0)  # if 'Newguy' is not in OrderedDict, then add ('Newguy', default_value) to OrderedDict
        od.setdefault('Bob', 0)
        print(od)

    def test_update(self):  # can be used to concatenate OrderedDicts
        print('update: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        od1 = {'Jane': 12, 'Newguy': 42}
        od.update(od1)
        print(od)

    def test_values(self):
        print('values: ', end='')
        mapping = {'Bob': 5, 'Alice': 8, 'George': 69, 'Jane': 3, 'Xavier': 1}
        od = OrderedDict(mapping)
        for v in od.values():
            print(v, ' ', end='')
        print()

    def test_OrderedDict(self):
        self.test_fromkeys()
        self.test_init_mapping()
        self.test_init_iterable()
        self.test_init_iterable2()
        self.test_init()
        self.test_contains()
        self.test_delitem()
        self.test_eq()
        self.test_getitem()
        self.test_iter()
        self.test_len()
        self.test_ne()
        self.test_repr()
        self.test_reversed()
        self.test_setitem()
        self.test_clear()
        self.test_copy()
        self.test_get()
        self.test_move_to_end()
        self.test_pop()
        self.test_popitem()
        self.test_setdefault()
        self.test_update()
        self.test_values()


if __name__ == '__main__':
    s = Solution()
    s.test_OrderedDict()
