from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        ds = defaultdict(int)
        for k in s:
            ds[k] += 1

        dt = defaultdict(int)
        for k in t:
            dt[k] += 1

        return ds == dt

    def print_answer(self, ans):
        print(ans)

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        ans = self.isAnagram(s, t)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
