def isBadVersion(version):
    return version == 4


class Solution(object):
    def firstBadVersion(self, n):
        i = -1
        l, r = 1, n
        while l <= r:
            m = (l+r)//2
            if isBadVersion(m):
                i = m
                r = m-1
            else:
                l = m+1
        return i

    def print_ans(self, ans):
        print(ans)

    def test(self):
        n = 5
        ans = self.firstBadVersion(n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
