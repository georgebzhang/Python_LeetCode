import heapq


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Room:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        room1 = Room(intervals[0].start, intervals[0].end)
        rooms = [(room1.end, room1)]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if rooms[0][0] < interval.start:
                heapq.heappop(rooms)

            room = Room(interval.start, interval.end)
            heapq.heappush(rooms, (room.end, room))

        return len(rooms)

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
