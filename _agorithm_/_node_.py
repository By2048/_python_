from loguru import logger


# 单链表节点
class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __bool__(self):
        return self.item is not None

    def __str__(self):
        return str(self.item).ljust(3)


# 双向链表节点
class BNode(Node):
    def __init__(self, item=None):
        self.previous = None
        super().__init__(item)


# 单向链表
class SingleLinkNode(object):
    def __init__(self):
        self.head: Node = Node()
        self.next: Node = Node()

    def __bool__(self):
        return bool(self.head)

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
        if not self:
            return 0
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
        # 头部添加
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        # 尾部添加
        node = Node(item)
        if not self:
            self.head = node
        else:
            current = self.head
            while current.next:
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
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def remove(self, item):
        current = self.head
        previous = None
        while current:
            if current.item == item:
                if not previous:  # 是第一个节点
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            else:  # 标记为移动
                previous = current
                current = current.next


# 循环链表
class SingleCycleLinkList(object):
    def __init__(self):
        self.head: Node = Node()
        self.next: Node = Node()

    def __bool__(self):
        return bool(self.head)

    def __len__(self):
        if not self:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        if not self:
            return
        current = self.head
        while current.next != self.head:
            yield current.item
            current = current.next
        yield current.item

    def __contains__(self, item):
        for _ in self:
            if item == _:
                return True
        return False

    def __str__(self):
        data = [str(item) for item in self]
        return ' '.join(data)

    def add(self, item):
        node = Node(item)
        if not self:
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
        self.head = node

    def append(self, item):
        node = Node(item)
        if not self:
            self.head = node
            node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        if index > len(self) - 1:
            self.append(item)
        else:
            node = Node(item)
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def remove(self, item):
        if not self:
            return
        current = self.head
        previous: Node = Node()

        if current.item == item:
            if current.next != self.head:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            else:
                self.head = None
        else:
            previous = self.head
            while current.next != self.head:
                if current.item != item:
                    previous = current
                    current = current.next
                else:
                    previous.next = current.next
                    return True
        if current.item == item:
            previous.next = self.head
            return True


# 双向链表
class BilateralLinkList(object):
    def __init__(self, item=None):
        self.head = item
        self.previous = None
        self.next = None

    def __bool__(self):
        return bool(self.head)

    def __contains__(self, item):
        for _ in self:
            if item == _:
                return True
        return False

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        data = [str(item) for item in self]
        return ' '.join(data)

    def __iter__(self):
        current = self.head
        while current:
            yield current.item
            current = current.next

    def add(self, item):
        node = BNode(item)
        if not self:
            self.head = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def append(self, item):
        node = BNode(item)
        if not self:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            node.previous = current
            current.next = node

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > len(self) - 1:
            self.append(item)
        else:
            node = BNode(item)
            current = self.head
            for i in range(index):
                current = current.next
            node.next = current
            node.previous = current.previous
            current.previous.next = node
            current.previous = node

    def remove(self, item):
        if not self:
            return

        current = self.head
        if current.item == item:
            if not current.next:
                self.head = BNode()
                return True
            else:
                self.head = current.next
                current.next.previous = BNode()
                return True

        while current.next:
            if current.item == item:
                current.previous.next = current.next
                current.next.previous = current.previous
                return True
            current = current.next

        if current.item == item:
            current.previous.next = BNode()
            return True


def test_node():
    node = Node()
    node1 = Node(1)

    logger.info(node)
    logger.info(node1)

    logger.info(bool(node))
    logger.info(bool(node1))


def test_single_link_node():
    #
    def test_1():
        node1 = Node(1)
        node2 = Node(2)
        logger.info(node1)
        logger.info(node2)

        data = SingleLinkNode()
        data.head = node1
        node1.next = node2
        logger.info(data.head.item)
        logger.info(data.head.next.item)

    def test_2():
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

    test_1()
    test_2()


def test_single_cycle_link_list():
    data = SingleCycleLinkList()

    logger.info(bool(data))

    for i in range(5):
        data.add(i)
    logger.info(data)

    data.append(6)
    logger.info(data)

    data.insert(3, 7)
    logger.info(data)

    data.remove(3)
    logger.info(data)

    logger.info(2 in data)
    logger.info(22 in data)


def test_bilateral_link_list():
    data = BilateralLinkList()

    logger.info(bool(data))

    for _ in range(5):
        data.add(_)
    logger.info(data)

    data.add(5)
    logger.info(data)

    data.append(6)
    logger.info(data)

    data.insert(3, 33)
    logger.info(data)

    data.remove(3)
    logger.info(data)

    logger.info(2 in data)
    logger.info(22 in data)


if __name__ == '__main__':
    pass
    # test_node()
    # test_single_link_node()
    # test_single_cycle_link_list()
    # test_single_cycle_link_list()
    # test_bilateral_link_list()
