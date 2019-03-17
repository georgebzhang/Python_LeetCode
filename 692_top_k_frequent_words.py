from collections import Counter
import heapq


class Solution(object):
    class Word(object):
        def __init__(self, s):
            self.s = s

        def __lt__(self, other):  # reverses lexicographical comparison of strings
            return self.s > other.s

    def topKFrequent(self, words, k):
        c = Counter(words)
        l = [(count, Solution.Word(word)) for word, count in c.items()]

        l_k = l[:k]
        heapq.heapify(l_k)

        for i in range(k, len(l)):
            heapq.heappushpop(l_k, l[i])

        l_k_sorted = []
        for i in range(k):
            l_k_sorted.append(heapq.heappop(l_k))
        l_k_sorted.reverse()

        result = [tup[1].s for tup in l_k_sorted]
        return result


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
