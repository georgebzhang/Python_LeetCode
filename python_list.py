class Solution(object):
    def test_add(self):
        print('add: ', end='')
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        print(l1 + l2)

    def test_contains(self):
        print('in: ', end='')
        l = [1, 2, 3, 4, 5]
        print(3 in l)

    def test_delitem(self):
        print('del: ', end='')
        l = [1, 2, 3, 4, 5]
        del l[2]
        print(l)

    def test_equals(self):
        print('==: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        print(l1 == l2)

    def test_ge(self):
        print('>=: ', end='')
        l1 = [1, 2, 4]
        l2 = [1, 2, 3]
        print(l1 >= l2)

    def test_getattribute(self):
        pass

    def test_getitem(self):
        print('getitem: ', end='')
        l = [1, 2, 3, 4, 5]
        print(l[2])

    def test_gt(self):
        print('>: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        print(l1 > l2)

    def test_iadd(self):  # MUTATES the list
        print('+=: ', end='')
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        # print(l1 += l2)  # cannot compile
        l1 += l2
        print(l1)

    def test_imul(self):
        print('*=: ', end='')
        l = [1, 2, 3]
        l *= 3
        print(l)

    def test_init(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        l = [1, 2, 3, 4, 5]
        i = iter(l)
        print(next(i), next(i), next(i))

    def test_le(self):
        print('<=: ', end='')
        l1 = [1, 2, 2]
        l2 = [1, 2, 3]
        print(l1 <= l2)

    def test_len(self):
        print('len: ', end='')
        l = [1, 2, 3]
        print(len(l))

    def test_lt(self):
        print('<: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        print(l1 < l2)

    def test_mul(self):
        print('*: ', end='')
        l = [1, 2, 3]
        print(l * 3)

    def test_ne(self):
        print('!=: ', end='')
        l1 = [1, 2, 2]
        l2 = [1, 2, 3]
        print(l1 != l2)

    def test_repr(self):
        print('repr: ', end='')
        l = [1, 2, 3]
        print(repr(l))

    def test_reversed(self):  # reversed iter
        print('reversed: ', end='')
        l = [1, 2, 3, 4, 5]
        r = reversed(l)
        print(next(r), next(r), next(r))

    def test_rmul(self):
        pass

    def test_setitem(self):
        print('setitem: ', end='')
        l = [1, 2, 3, 4, 5]
        l[2] = 69
        print(l)

    def test_sizeof(self):
        pass

    def test_append(self):
        print('append: ', end='')
        l = [1, 2, 3]
        l.append(4)
        print(l)

    def test_clear(self):
        print('clear: ', end='')
        l = [1, 2, 3]
        l.clear()
        print(l)

    def test_copy(self):
        print('copy: ', end='')
        l1 = [1, 2, 3]
        l2 = l1.copy()
        # print(id(l1))
        # print(id(l2))
        print(l2)
        # print(l1 == l2)
        # print(l1 is l2)

    def test_count(self):
        print('count: ', end='')
        l = [1, 2, 3, 2, 2, 4]
        print(l.count(2))

    def test_extend(self):
        print('extend: ', end='')
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        l1.extend(l2)
        print(l1)

    def test_index(self):
        print('index: ', end='')
        l = [1, 2, 3, 4, 3]
        print(l.index(3))

    def test_insert(self):
        print('insert: ', end='')
        l = [1, 2, 3, 4, 5]
        l.insert(1, 69)
        print(l)

    def test_pop(self):
        print('pop: ', end='')
        l = [1, 2, 3, 4, 5]
        print(l.pop(), l)

    def test_remove(self):
        print('remove: ', end='')
        l = [1, 2, 3, 3, 3]
        l.remove(3)
        print(l)

    def test_reverse(self):
        print('reverse: ', end='')
        l = [1, 2, 3, 4, 5]
        l.reverse()
        print(l)

    def test_sort(self):
        print('sort: ', end='')
        l = [6, 1, 8, 3, 2]
        l.sort()
        print(l)

    def test_list(self):
        self.test_add()
        self.test_contains()
        self.test_delitem()
        self.test_equals()
        self.test_ge()
        self.test_getitem()
        self.test_gt()
        self.test_iadd()
        self.test_imul()
        self.test_iter()
        self.test_le()
        self.test_len()
        self.test_lt()
        self.test_mul()
        self.test_ne()
        self.test_repr()
        self.test_reversed()
        self.test_setitem()
        self.test_append()
        self.test_clear()
        self.test_copy()
        self.test_count()
        self.test_extend()
        self.test_index()
        self.test_insert()
        self.test_pop()
        self.test_remove()
        self.test_reverse()
        self.test_sort()


if __name__ == '__main__':
    s = Solution()
    s.test_list()
