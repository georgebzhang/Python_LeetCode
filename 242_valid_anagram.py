from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        cs = Counter(s)
        ct = Counter(t)
        return cs == ct

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
