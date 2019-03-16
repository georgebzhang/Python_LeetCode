from itertools import permutations
from collections import deque


class Solution(object):
    def print_perms(self, perms):
        for p in perms:
            print(p, ' ', end= '')
        print()

    def swap(self, l, ind1, ind2):
        l[ind1], l[ind2] = l[ind2], l[ind1]

    def permutations0(self, l):
        def permutations0_helper(l, ind_left, ind_right):  # helper function nested inside calling function
            if ind_left == ind_right:
                perms.append(l.copy())  # MUST USE COPY, OTHERWISE l WILL UPDATE AND ALL ITEMS IN LIST WILL UPDATE

            for i in range(ind_left, ind_right + 1):
                self.swap(l, ind_left, i)
                permutations0_helper(l, ind_left + 1, ind_right)
                self.swap(l, ind_left, i)

        perms = []  # list to contain all permutations
        n = len(l)
        permutations0_helper(l, 0, n - 1)
        return perms

    def permutations1_helper(self, perms, l, ind_left, ind_right):  # helper function outside calling function
        if ind_left == ind_right:
            perms.append(l.copy())  # MUST USE COPY, OTHERWISE l WILL UPDATE AND ALL ITEMS IN LIST WILL UPDATE

        for i in range(ind_left, ind_right + 1):
            self.swap(l, ind_left, i)
            self.permutations1_helper(perms, l, ind_left + 1, ind_right)
            self.swap(l, ind_left, i)

    def permutations1(self, l):
        perms = []  # list to contain all permutations
        n = len(l)
        self.permutations1_helper(perms, l, 0, n - 1)
        return perms

    def permutations2(self, l):
        n = len(l)
        if n == 0:
            return []
        if n == 1:
            return [l]

        perms = []
        for i in range(len(l)):
            m = l[i]
            rem = l[:i] + l[i+1:]
            for p in self.permutations2(rem):
                perms.append([m] + p)

        return perms

    def permutations3(self, l):  # iterative
        perms = deque()
        perms.append([])

        if l:
            for i in range(len(l)):
                while len(perms[0]) == i:
                    temp = perms.popleft()

                    l_copy = l.copy()
                    for item in temp:
                        l_copy.remove(item)

                    for item in l_copy:
                        perms.append(temp + [item])

        return perms

    def permutations4(self, l):  # using Python itertools permutations
        perms = permutations(l)
        return perms

    def test(self):
        l = ['a', 'b', 'c']

        perms = self.permutations0(l)
        # self.print_perms(perms)

        perms = self.permutations1(l)
        # self.print_perms(perms)

        perms = self.permutations2(l)
        # self.print_perms(perms)

        perms = self.permutations3(l)
        self.print_perms(perms)

        perms = self.permutations4(l)
        # self.print_perms(perms)


if __name__ == '__main__':
    s = Solution()
    s.test()
