import sys


class Solution(object):
    def swap(self, arr, ind1, ind2):
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]

    def findKthLargest(self, nums, k):  # actually find kth smallest
        def partition(arr, ind_l, ind_r):
            ind_pivot = ind_r
            val_pivot = arr[ind_pivot]
            ind_partition = ind_l

            for i in range(ind_l, ind_r):
                if arr[i] <= val_pivot:
                    self.swap(arr, i, ind_partition)
                    ind_partition += 1

            self.swap(arr, ind_partition, ind_pivot)
            return ind_partition

        def findKthLargest_rec(arr, ind_l, ind_r, k):
            if k > 0 and k <= ind_r - ind_l + 1:
                ind_partition = partition(arr, ind_l, ind_r)
                if k - 1 == ind_partition - ind_l:
                    return arr[ind_partition]
                elif k - 1 < ind_partition - ind_l:
                    return findKthLargest_rec(arr, ind_l, ind_partition - 1, k)
                else:
                    return findKthLargest_rec(arr, ind_partition + 1, ind_r, k - ind_partition + ind_l - 1)
            return sys.maxsize

        nums = [-n for n in nums]  # convert find kth smallest into find kth largest
        n = len(nums)
        return -findKthLargest_rec(nums, 0, n - 1, k)  # convert find kth smallest into find kth largest

    def print_ans(self, ans):
        print(ans)

    def test(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        ans = self.findKthLargest(nums, k)
        self.print_ans(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
