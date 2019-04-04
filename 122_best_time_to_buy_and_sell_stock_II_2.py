class Solution(object):
    def maxProfit(self, prices):
        result = 0
        increases = []  # list of tuples
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                increases.append((prices[i], prices[i+1]))
        # print(increases)

        for increase in increases:
            result += increase[1] - increase[0]
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
