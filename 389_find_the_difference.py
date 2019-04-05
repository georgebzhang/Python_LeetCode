from collections import Counter


class Solution(object):
    def findTheDifference(self, s, t):
        s = Counter(s)
        t = Counter(t)
        for k in t:
            if k not in s:
                return k
            if t[k] > s[k]:
                return k

    def print_ans(self, ans):
        print(ans)

    def test(self):
        s = 'abcd'
        t = 'abcde'
        ans = self.findTheDifference(s, t)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
