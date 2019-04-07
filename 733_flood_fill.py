class Point:  # making Point class not too useful here, because 2 points with same r, c are unique, so set visited contains tuples (r, c)
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def neighbors(self, r_len, c_len):
        neighbors = []
        if self.r - 1 >= 0:
            neighbors.append(Point(self.r - 1, self.c))
        if self.r + 1 < r_len:
            neighbors.append(Point(self.r + 1, self.c))
        if self.c - 1 >= 0:
            neighbors.append(Point(self.r, self.c - 1))
        if self.c + 1 < c_len:
            neighbors.append(Point(self.r, self.c + 1))
        return neighbors


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        def dfs(p):
            if (p.r, p.c) in visited:
                return
            visited.add((p.r, p.c))
            if image[p.r][p.c] != color[0]:
                return
            image[p.r][p.c] = newColor
            for n in p.neighbors(image_dim[0], image_dim[1]):
                dfs(n)

        visited = set()
        image_dim = (len(image), len(image[0]))
        color = [image[sr][sc]]
        dfs(Point(sr, sc))
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
