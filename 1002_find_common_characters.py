from collections import Counter


class Solution(object):
    def commonChars(self, A):
        result = []
        cs = [Counter(a) for a in A]
        for k in cs[0]:
            result += [k] * min(c[k] for c in cs)

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        A = ["bella", "label", "roller"]
        ans = self.commonChars(A)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
