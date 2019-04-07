from collections import deque


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        def neighbors(p):
            neighbors = []
            r, c = p
            if r-1 >= 0:
                neighbors.append((r-1, c))
            if r+1 < len(image):
                neighbors.append((r+1, c))
            if c-1 >= 0:
                neighbors.append((r, c-1))
            if c+1 < len(image[0]):
                neighbors.append((r, c+1))
            return neighbors

        visited = set()
        color = image[sr][sc]
        p = (sr, sc)
        q = deque()
        q.append(p)
        while q:
            p = q.popleft()
            if p in visited:
                continue
            visited.add(p)
            r, c = p
            if image[r][c] != color:
                continue
            image[r][c] = newColor
            for n in neighbors(p):
                q.append(n)

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
