from collections import defaultdict


class Solution(object):
    def test_init_lambda(self):
        print('defaultdict(lambda): ', end='')
        dd = defaultdict(lambda: 'DEFAULT_VALUE')  # default value is DEFAULT_VALUE
        dd['Bob'] = 'awesome'
        print(dd['Bob'], dd['George'])

    def test_init_list(self):
        print('defaultdict(list): ', end='')
        dd = defaultdict(list)  # default value is empty list []
        transaction_record = [('George', 5), ('Bob', 7), ('Alice', 3), ('George', 6), ('Alice', 9)]
        for k, v in transaction_record:
            dd[k].append(v)
        print(dd)

    def test_init_int(self):
        print('defaultdict(list): ', end='')
        dd = defaultdict(int)  # default value is 0
        transaction_record = [('George', 5), ('Bob', 7), ('Alice', 3), ('George', 6), ('Alice', 9)]
        for k, v in transaction_record:
            dd[k] += v
        print(dd)

    def test_defaultdict(self):
        self.test_init_lambda()
        self.test_init_list()
        self.test_init_int()


if __name__ == '__main__':
    s = Solution()
    s.test_defaultdict()
