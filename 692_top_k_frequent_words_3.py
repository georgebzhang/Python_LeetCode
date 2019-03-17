from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, words, k):
        c = Counter(words)
        return heapq.nsmallest(k, c, key=lambda word: (~c[word], word))

    def print_ans(self, ans):
        print(ans)

    def test(self):
        words = ['aaa', 'aa', 'a']
        k = 2
        ans = self.topKFrequent(words, k)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
