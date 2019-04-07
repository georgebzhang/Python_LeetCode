class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # {key: ListNode(key, value)}
        self.head, self.tail = ListNode(None, None), ListNode(None, None)  # dummy head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return len(self.map)

    def add(self, n):
        next = self.head.next
        self.head.next = n
        n.prev = self.head
        n.next = next
        next.prev = n

    def remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev

    def get(self, key: int) -> int:
        try:
            n = self.map[key]
            self.remove(n)
            self.add(n)
            return n.value
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            n = self.map[key]
            n.value = value
            self.remove(n)
            self.add(n)
            return

        if len(self) == self.capacity:
            n_lru = self.tail.prev
            self.remove(n_lru)
            key_lru = n_lru.key
            del self.map[key_lru]

        n = ListNode(key, value)
        self.map[key] = n
        self.add(n)


class Solution(object):
    def print_answer(self, ans):
        print(ans)

    def test(self):
        commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        commands_params = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

        output = []
        answer = [None, None, None, 1, None, -1, None, -1, 3, 4]
        print(answer)

        obj = None
        if commands[0] == 'LRUCache':
            obj = LRUCache(*commands_params[0])
            output.append(None)
        else:
            raise Exception('LRUCache not initialized!')

        for i in range(1, len(commands)):
            command = commands[i]
            if command == 'put':
                output.append(obj.put(*commands_params[i]))
            elif command == 'get':
                output.append(obj.get(*commands_params[i]))
            else:
                raise Exception('Invalid command!')
        print(output)
        self.print_answer(output == answer)


if __name__ == '__main__':
    s = Solution()
    s.test()
