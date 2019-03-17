from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        c = Counter(s)
        l = [(v, k) for k, v in c.items()]
        l.sort(reverse=True)
        return ''.join(char * count for count, char in l)

    def print_ans(self, ans):
        print(ans)

    def test(self):
        s = 'tree'
        ans = self.frequencySort(s)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
