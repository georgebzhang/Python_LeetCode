class Solution(object):
    def test_list_square(self):
        print('square: ', end='')
        l1 = [1, 2, 3, 4, 5]
        l2 = [num ** 2 for num in l1]  # acts as map
        print(l2)

    def test_list_even(self):
        print('even: ', end='')
        l1 = [1, 2, 3, 4, 5]
        l2 = [num for num in l1 if num % 2 == 0]  # acts as filter
        print(l2)

    def test_list_pair(self):
        print('pair: ', end='')
        l1 = ['a', 'b', 'c']
        l2 = [(let, num) for let in l1 for num in range(3)]
        print(l2)

    def test_dict(self):
        names = ['Bruce', 'Clark', 'Peter']
        heros = ['Batman', 'Superman', 'Spiderman']
        d = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
        print(d)

    def test_set(self):
        l = [1, 1, 2, 3, 4, 4, 5]
        s = {num for num in l}  # or just s = set(l)
        print(s)

    def test_generator(self):
        l = [1, 2, 3, 4, 5]
        gen = (num ** 2 for num in l)  # list comprehension for a generator, NOT a tuple. For tuple, use tuple(expression)
        for i in gen:
            print(i, ' ', end='')
        print(type(gen))

    def test_list_comprehension(self):
        self.test_list_square()
        self.test_list_even()
        self.test_list_pair()
        self.test_dict()
        self.test_set()
        self.test_generator()


if __name__ == '__main__':
    s = Solution()
    s.test_list_comprehension()
