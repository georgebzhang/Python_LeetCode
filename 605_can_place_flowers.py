class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        def canPlaceAt(ind):
            left_empty, curr_empty, right_empty = True, flowerbed[ind] == 0, True
            if ind == 0:
                right_empty = flowerbed[1] == 0
            elif ind == len(flowerbed)-1:
                left_empty = flowerbed[-2] == 0
            else:
                left_empty = flowerbed[ind-1] == 0
                right_empty = flowerbed[ind+1] == 0
            return left_empty and curr_empty and right_empty

        if n == 0:
            return True
        if not flowerbed:
            return n == 0
        m = len(flowerbed)
        if m == 1:
            return (n <= 1 and flowerbed[0] == 0) or (n == 0 and flowerbed[0] == 1)

        for i in range(m):
            if canPlaceAt(i):
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True

        return False

    def print_ans(self, ans):
        print(ans)

    def test(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        ans = self.canPlaceFlowers(flowerbed, n)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
