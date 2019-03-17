from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        c = Counter(s)
        l = [(k, v) for k, v in c.items()]
        l.sort(key=lambda kv: -kv[1])
        result = ''
        for i in range(len(l)):
            for j in range(l[i][1]):
                result += l[i][0]
        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        s = 'tree'
        ans = self.frequencySort(s)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
