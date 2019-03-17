class Solution(object):
    def readBinaryWatch(self, num):
        def bit_count(n):
            return bin(n).count('1')

        result = []
        for hour in range(12):
            for minute in range(60):
                if bit_count(hour) + bit_count(minute) == num:
                    result.append('{}:{}'.format(hour, str(minute).zfill(2)))

        return result

    def print_ans(self, ans):
        print(ans)

    def test(self):
        num = 2
        ans = self.readBinaryWatch(num)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
