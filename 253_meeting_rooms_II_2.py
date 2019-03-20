from heapq import heappop, heappush


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        ends = []  # min heap on end times

        for interval in intervals:
            if ends and ends[0] < interval.start:
                heappop(ends)
            heappush(ends, interval.end)  # must push for every interval

        return len(ends)

    def print_answer(self, ans):
        print(ans)

    def test(self):
        input = [[0, 30], [5, 10], [15, 20]]
        intervals = []
        for s, e in input:
            interval = Interval(s, e)
            intervals.append(interval)
        ans = self.minMeetingRooms(intervals)
        self.print_answer(ans)


if __name__ == '__main__':
    s = Solution()
    s.test()
