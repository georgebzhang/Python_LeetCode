class Solution(object):
    def test_add(self):
        print('+: ', end='')
        s1 = 'hello '
        s2 = 'my'
        s1 = s1 + s2
        print(s1)

    def test_contains(self):
        print('in: ', end='')
        s = 'hello my name is george'
        print('my' in s)

    def test_equals(self):
        print('==: ', end='')
        s = 'hello'
        t = 'hello'
        print(s == t)

    def test_format(self):
        pass

    def test_ge(self):
        print('>=: ', end='')
        s = 'iello'
        t = 'hello'
        print(s >= t)

    def test_getattribute(self):
        pass

    def test_getitem(self):
        print('getitem: ', end='')
        s = 'hello'
        print(s[4])

    def test_getnewargs(self):
        pass

    def test_gt(self):
        print('>: ', end='')
        s = 'iello'
        t = 'hello'
        print(s > t)

    def test_hash(self):
        pass

    def test_iter(self):
        print('iter: ', end='')
        s = 'hello'
        i = iter(s)
        print(next(i), next(i), next(i))

    def test_le(self):
        print('<=: ', end='')
        s = 'iello'
        t = 'hello'
        print(s <= t)

    def test_len(self):
        print('len: ', end='')
        s = 'hello'
        print(len(s))

    def test_lt(self):
        print('<: ', end='')
        s = 'iello'
        t = 'hello'
        print(s < t)

    def test_mod(self):
        pass

    def test_mult(self):
        print('*: ', end='')
        s = 'hello'
        print(s * 3)

    def test_ne(self):
        print('!=: ', end='')
        s = 'iello'
        t = 'hello'
        print(s != t)

    def test_repr(self):
        print('repr: ', end='')
        s = 'hello'
        print(repr(s))

    def test_rmod(self):
        pass

    def test_rmul(self):
        pass

    def test_sizeof(self):
        pass

    def test_capitalize(self):
        print('capitalize: ', end='')
        s = 'hello my name is george'
        s = s.capitalize()
        print(s)

    def test_casefold(self):
        print('casefold: ', end='')
        s = 'HelLo My nAme is gEoRGe'
        s = s.casefold()
        print(s)

    def test_center(self):
        pass

    def test_count(self):
        print('count: ', end='')
        s = 'hello my namE is gEorge'
        print(s.count('e'))

    def test_encode(self):
        pass

    def test_endswith(self):
        print('endswith: ', end='')
        s = 'hello my name is george'
        print(s.endswith('eorge'))

    def test_expandtabs(self):
        pass

    def test_find(self):
        print('find: ', end='')
        s = 'hello my name is george'
        i = s.find('e')
        print(i)

    def test_format(self):
        pass

    def test_format_map(self):
        pass

    def test_index(self):
        print('index: ', end='')
        s = 'hello my name is george'
        t = ' my nam'
        print(s.index(t))

    def test_isalnum(self):
        print('isalnum: ', end='')
        s = 'hello69'
        print(s.isalnum())

    def test_isalpha(self):
        print('isalpha: ', end='')
        s = 'hello69'
        print(s.isalpha())

    def test_isascii(self):
        print('isascii: ', end='')
        s = 'hello69!@#$'
        print(s.isascii())

    def test_isdecimal(self):
        print('isdecimal: ', end='')
        s = '1234567890'
        print(s.isdecimal())

    def test_isdigit(self):
        print('isdigit: ', end='')
        s = '1234567890'
        print(s.isdigit())

    def test_isidentifier(self):
        pass

    def test_islower(self):
        print('islower: ', end='')
        s = 'hellO'
        print(s.islower())

    def test_isnumeric(self):
        print('isnumeric: ', end='')
        s = '1234567890'
        print(s.isnumeric())

    def test_isprintable(self):
        pass

    def test_isspace(self):
        print('isspace: ', end='')
        s = '     '
        print(s.isspace())

    def test_istitle(self):
        print('istitle: ', end='')
        s = 'Hello My Name Is George'
        print(s.istitle())

    def test_isupper(self):
        print('isupper: ', end='')
        s = 'HELLO'
        print(s.isupper())

    def test_join(self):
        print('join: ', end='')
        s = 'abcdefghi'
        l = list(s)
        del l[1]
        s = ''.join(l)
        print(s)

    def test_ljust(self):
        print('ljust: ', end='')
        s = 'Hello'
        print(s.ljust(10, '#'))

    def test_lower(self):
        print('lower: ', end='')
        s = 'HelLo'
        print(s.lower())

    def test_lstrip(self):
        print('lstrip: ', end='')
        s = '     hello'
        print(s.lstrip())

    def test_partition(self):
        print('partition: ', end='')
        s = 'hello'
        print(s.partition('ll'))

    def test_replace(self):
        print('replace: ', end='')
        s = 'I don\'t want whitespace'
        print(s.replace(' ', ''))

    def test_rfind(self):
        print('rfind: ', end='')
        s = 'Hello'
        print(s.rfind('l'))

    def test_rindex(self):
        print('rindex: ', end='')
        s = 'Hello hello'
        print(s.rindex('llo'))

    def test_rjust(self):
        print('rjust: ', end='')
        s = 'Hello'
        print(s.rjust(10))

    def test_rpartition(self):
        print('rpartition: ', end='')
        s = 'Hello'
        print(s.rpartition('ll'))

    def test_rsplit(self):
        print('rsplit: ', end='')
        s = 'apples, oranges, bananas'
        print(s.rsplit(', '))

    def test_split(self):
        print('split: ', end='')
        s = 'apples, oranges, bananas'
        print(s.split(', '))

    def test_splitlines(self):
        print('split: ', end='')
        s = 'apples\noranges\nbananas'
        print(s.splitlines())

    def test_startswith(self):
        print('startswith: ', end='')
        s = 'hello my name is george'
        print(s.startswith('hello m'))

    def test_strip(self):
        print('strip: ', end='')
        s = '     Hello     '
        print(s.strip())

    def test_swapcase(self):
        print('swapcase: ', end='')
        s = 'Hello'
        print(s.swapcase())

    def test_title(self):
        print('title: ', end='')
        s = 'hello my name is george'
        print(s.title())

    def test_translate(self):
        pass

    def test_upper(self):
        print('upper: ', end='')
        s = 'hEllo'
        print(s.upper())

    def test_zfill(self):
        print('zfill: ', end='')
        s = '69x'
        print(s.zfill(5))

    def test_string(self):
        self.test_add()
        self.test_contains()
        self.test_equals()
        self.test_ge()
        self.test_getitem()
        self.test_gt()
        self.test_iter()
        self.test_le()
        self.test_len()
        self.test_lt()
        self.test_mult()
        self.test_ne()
        self.test_repr()
        self.test_capitalize()
        self.test_casefold()
        self.test_count()
        self.test_endswith()
        self.test_find()
        self.test_index()
        self.test_isalnum()
        self.test_isalpha()
        self.test_isascii()
        self.test_isdecimal()
        self.test_isdigit()
        self.test_islower()
        self.test_isnumeric()
        self.test_isspace()
        self.test_istitle()
        self.test_isupper()
        self.test_join()
        self.test_ljust()
        self.test_lower()
        self.test_lstrip()
        self.test_partition()
        self.test_replace()
        self.test_rfind()
        self.test_rindex()
        self.test_rjust()
        self.test_rpartition()
        self.test_rsplit()
        self.test_split()
        self.test_splitlines()
        self.test_startswith()
        self.test_strip()
        self.test_swapcase()
        self.test_title()
        self.test_upper()
        self.test_zfill()


if __name__ == '__main__':
    s = Solution()
    s.test_string()
