from collections import Counter


class Solution(object):
    def commonChars(self, A):
        c = Counter(A[0])
        for a in A:
            c &= Counter(a)

        return list(c.elements())

    def print_ans(self, ans):
        print(ans)

    def test(self):
        A = ["bella", "label", "roller"]
        ans = self.commonChars(A)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
