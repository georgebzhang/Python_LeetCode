class Solution(object):
    def mySqrt(self, x):
        result = -1
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            if m * m < x:
                result = m
                l = m + 1
            elif m * m > x:
                r = m - 1
            else:
                return m
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        x = 8
        ans = self.mySqrt(x)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
