class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        m = len(flowerbed)
        for i in range(m):
            left = i-1 if i > 0 else 0  # force left to start if i is start
            right = i+1 if i < m-1 else m-1  # force right to end if i is end
            if flowerbed[i] == 0 and flowerbed[left] == 0 and flowerbed[right] == 0:
                flowerbed[i] = 1
                count += 1
            if count >= n:  # ends loop early
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
