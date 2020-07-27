from loguru import logger


class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkNode(object):
    def __init__(self):
        self.head = None
        self.next = None

    def __bool__(self):
        return self.head is None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.item
            node = node.next

    def __contains__(self, item):
        for _ in self:
            if item == _:
                return True
        return False

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def __str__(self):
        data = [str(item) for item in self]
        return ' '.join(data)

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        node = Node(item)
        if self:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index >= (len(self) - 1):
            self.append(item)
        else:
            node = Node(item)
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.item == item:
                if not previous:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            else:
                previous = current
                current = current.next


def test():
    data = SingleLinkNode()

    data.add(1)
    data.add(2)
    data.append(3)
    data.append(4)

    logger.info(data)
    logger.info(len(data))

    logger.info(4 in data)
    logger.info(5 in data)

    data.insert(2, -1)
    logger.info(data)

    data.remove(4)
    logger.info(data)


if __name__ == '__main__':
    test()
