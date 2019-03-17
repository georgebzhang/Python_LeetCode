import heapq


class Solution(object):
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class PersonHeap(object):
        def __init__(self, l_init=None, key=lambda person: person.age):  # -person.age for max heap on age
            self.key = key
            if l_init:
                self._data = [(key(person), person) for person in l_init]
                heapq.heapify(self._data)
            else:
                self._data = []

        def push(self, person):
            heapq.heappush(self._data, (self.key(person), person))

        def pop(self):
            return heapq.heappop(self._data)[1]

        def peek(self):
            return self._data[0][1]

        def heappushpop(self, person):  # good for heaps of fixed size
            return heapq.heappushpop(self._data, (self.key(person), person))[1]

    def test_personheap(self):
        names = ['George', 'Alice', 'Bob', 'Jane', 'Will']
        ages = [24, 17, 12, 45, 30]
        l_init = []
        for i in range(len(names)):
            p = Solution.Person(names[i], ages[i])
            l_init.append(p)
        ph = Solution.PersonHeap(l_init)
        print(ph.peek().age)
        # print(ph.pop())
        # print(ph.heappushpop(Solution.Person('Max', 19)))

    def test_heapq(self):
        self.test_personheap()


if __name__ == '__main__':
    s = Solution()
    s.test_heapq()
