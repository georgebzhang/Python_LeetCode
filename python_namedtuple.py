from collections import namedtuple


class Solution(object):
    def test_init(self):
        print('init: ', end='')
        Person = namedtuple('Person', ['name', 'age'])
        p0 = Person('Bob', 36)
        p1 = Person(name='Alice', age=27)
        print(p0, p1)

    def test_unpack(self):
        print('unpack: ', end='')
        Person = namedtuple('Person', ['name', 'age'])
        p = Person('Bob', 36)
        n, a = p
        print(n, a)

    def test_access_by_field(self):
        print('access by field: ', end='')
        Person = namedtuple('Person', ['name', 'age'])
        p = Person('Bob', 36)
        print(p.name, p.age)

    def test_asdict(self):
        print('asdict: ', end='')
        Person = namedtuple('Person', ['name', 'age'])
        p = Person('Bob', 36)
        d = p._asdict()
        print(d)

    def test_replace(self):
        print('replace: ', end='')
        Person = namedtuple('Person', ['name', 'age'])
        p = Person('Bob', 36)
        p = p._replace(name='George')  # tuple is immutable, so must make a copy and reassign
        print(p)

    def test_namedtuple(self):
        self.test_init()
        self.test_unpack()
        self.test_access_by_field()
        self.test_asdict()
        self.test_replace()


if __name__ == '__main__':
    s = Solution()
    s.test_namedtuple()
