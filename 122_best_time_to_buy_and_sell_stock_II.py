class Solution(object):
    def maxProfit(self, prices):
        result = 0
        increasing = []
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                increasing.append(prices[i])
                increasing.append(prices[i+1])
        # print(increasing)

        for i in range(0, len(increasing), 2):
            result += increasing[i+1] - increasing[i]
        return result

    def print_answer(self, ans):
        print(ans)

    def test(self):
        prices = [7, 1, 5, 3, 6, 4]
        ans = self.maxProfit(prices)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
