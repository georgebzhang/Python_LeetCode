class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        M, N = len(image), len(image[0])
        color = image[sr][sc]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def neighbors(i0, j0):
            result = []
            for di, dj in dirs:
                i, j = i0 + di, j0 + dj
                if 0 <= i < N and 0 <= j < M and image[j][i] == color:
                    result.append((i, j))
            return result

        def dfs(i, j):
            p = (i, j)
            if p in visited:
                return
            visited.add(p)
            image[j][i] = newColor
            for n in neighbors(*p):
                dfs(*n)

        visited = set()
        dfs(sc, sr)
        return image

    def print_image(self, image):
        for row in image:
            print(row)

    def print_ans(self, ans):
        self.print_image(ans)

    def test(self):
        image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        sr = 1
        sc = 1
        newColor = 2
        self.print_image(image)
        print()
        ans = self.floodFill(image, sr, sc, newColor)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
