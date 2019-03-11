from collections import deque


class Solution(object):
    def test_init(self):
        print('deque(): ', end='')
        dq = deque()
        print(dq)

    def test_init_iterable(self):
        print('deque(iterable): ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(dq)

    def test_add(self):
        print('+: ', end='')
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        dq1 = deque(l1)
        dq2 = deque(l2)
        dq = dq1 + dq2
        print(dq)

    def test_bool(self):
        print('bool: ', end='')
        l = [1, 2, 3, 4, 5]
        dq1 = deque(l)
        dq2 = deque()
        print(not dq1, not dq2)

    def test_contains(self):
        print('in: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(3 in dq)

    def test_copy(self):
        print('copy: ', end='')
        l = [1, 2, 3, 4, 5]
        dq1 = deque(l)
        dq2 = dq1.copy()
        print(dq2)

    def test_delitem(self):
        print('copy: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        del dq[2]
        print(dq)

    def test_eq(self):
        print('==: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        dq1 = deque(l1)
        dq2 = deque(l2)
        print(dq1 == dq2)

    def test_ge(self):
        print('>=: ', end='')
        l1 = [1, 2, 4]
        l2 = [1, 2, 3]
        dq1 = deque(l1)
        dq2 = deque(l2)
        print(dq1 >= dq2)

    def test_getattributes(self):
        pass

    def test_getitem(self):
        print('copy: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(dq[2])

    def test_gt(self):
        print('>: ', end='')
        l1 = [1, 2, 4]
        l2 = [1, 2, 3]
        dq1 = deque(l1)
        dq2 = deque(l2)
        print(dq1 > dq2)

    def test_iadd(self):
        print('+=: ', end='')
        l1 = [1, 2, 3]
        l2 = [4, 5, 6]
        dq1 = deque(l1)
        dq2 = deque(l2)
        dq1 += dq2
        print(dq1)

    def test_imul(self):
        print('*=: ', end='')
        l = [1, 2, 3]
        dq = deque(l)
        dq *= 3
        print(dq)

    def test_iter(self):
        print('iter: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        i = iter(dq)
        print(next(i), next(i), next(i))

    def test_le(self):
        print('<=: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 2]
        dq1 = deque(l1)
        dq2 = deque(l2)
        print(dq1 <= dq2)

    def test_len(self):
        print('len: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(len(dq))

    def test_lt(self):
        print('<: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 2]
        dq1 = deque(l1)
        dq2 = deque(l2)
        print(dq1 < dq2)

    def test_mul(self):
        print('*: ', end='')
        l = [1, 2, 3]
        dq1 = deque(l)
        dq = dq1 * 3
        print(dq)

    def test_ne(self):
        print('!=: ', end='')
        l1 = [1, 2, 3]
        l2 = [1, 2, 3]
        dq1 = deque(l1)
        dq2 = deque(l2)
        print(dq1 != dq2)

    def test_reduce(self):
        pass

    def test_repr(self):
        print('repr: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(repr(dq))

    def test_reversed(self):
        print('reversed: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        i = reversed(dq)
        print(next(i), next(i), next(i))

    def test_rmul(self):
        pass

    def test_setitem(self):
        print('[] =: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        dq[2] = 69
        print(dq)

    def test_sizeof(self):
        pass

    def test_append(self):
        print('append: ', end='')
        l = [1, 2, 3]
        dq = deque(l)
        dq.append(4)
        print(dq)

    def test_appendleft(self):
        print('appendleft: ', end='')
        l = [1, 2, 3]
        dq = deque(l)
        dq.appendleft(0)
        print(dq)

    def test_clear(self):
        print('clear: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        dq.clear()
        print(dq)

    def test_index(self):
        print('index: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(dq.index(3))

    def test_insert(self):
        print('insert: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        dq.insert(2, 69)
        print(dq)

    def test_pop(self):
        print('pop: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(dq.pop(), dq)

    def test_popleft(self):
        print('popleft: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        print(dq.popleft(), dq)

    def test_remove(self):
        print('remove: ', end='')
        l = [1, 2, 3, 4, 5, 3]
        dq = deque(l)
        dq.remove(3)
        print(dq)

    def test_reverse(self):
        print('reverse: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        dq.reverse()
        print(dq)

    def test_rotate(self):
        print('rotate: ', end='')
        l = [1, 2, 3, 4, 5]
        dq = deque(l)
        dq.rotate(2)
        print(dq)

    def test_deque(self):
        self.test_init()
        self.test_init_iterable()
        self.test_add()
        self.test_bool()
        self.test_contains()
        self.test_copy()
        self.test_delitem()
        self.test_eq()
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
        self.test_appendleft()
        self.test_clear()
        self.test_index()
        self.test_insert()
        self.test_pop()
        self.test_popleft()
        self.test_remove()
        self.test_reverse()
        self.test_rotate()


if __name__ == '__main__':
    s = Solution()
    s.test_deque()
