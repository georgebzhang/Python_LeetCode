class Solution(object):
    def maxProfit(self, prices):
        increases = []  # list of tuples
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                increases.append((prices[i], prices[i+1]))

        if not increases:
            return 0

        n = len(increases)
        if n == 1:
            return increases[0][1]-increases[0][0]
        result = 0
        for i in range(n):
            for j in range(i, n):
                diff = increases[j][1] - increases[i][0]
                if diff > result:
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
