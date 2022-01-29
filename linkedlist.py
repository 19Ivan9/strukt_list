from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    # head->[2]->[4]->[6]->[10]->[]
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ''
        while cur_node != None:
            output += str(cur_node.get_data()) + '->'
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        return count

    def push(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def pop(self):
        cur_node = self.head
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def index(self, index):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range!')

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.push(data)
                return
            elif count + 1 == index:
                node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range!')

    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() != None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                node_to_remove = cur_node.get_next()
                node_after_removed = node_to_remove.get_next()
                cur_node.set_next(node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print('Index is out of range!')

    def reverse(self):
        prev = None
        cur_node = self.head
        next = None
        while cur_node != None:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev

    def slice(self, index_1=0, index_2=0):
        if index_1 > self.length() or index_2 > self.length():
            raise IndexError('Index is out of range!')
        cur_node = self.head
        counter = 0
        output = ''
        if index_1 == 0 and index_2 == 0:
            self.show()
        elif index_1 != 0:
            while counter < index_1:
                cur_node = cur_node.get_next()
                counter += 1
        while counter < index_2:
            output += str(cur_node.get_data()) + '->'
            cur_node = cur_node.get_next()
            counter += 1
        print(output)
