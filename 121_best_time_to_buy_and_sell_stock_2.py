class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        result = 0
        for i in range(1, len(prices)):
            curr_price = prices[i]
            diff = curr_price-min_price
            if curr_price < min_price:
                min_price = curr_price
            elif diff > result:
                result = diff
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
