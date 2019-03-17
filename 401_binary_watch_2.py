class Solution(object):
    def readBinaryWatch(self, num):
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        result = []
        backtrack(result, [0, 0], )

    def print_ans(self, ans):
        print(ans)

    def test(self):
        pass


if __name__ == '__main__':
    s = Solution()
    s.test()
