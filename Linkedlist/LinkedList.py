class Node:
    '''Implements a node that stores the value and pointer to next node.'''

    def __init__(self, data):
        self._data = data
        self._nextLink = None

    def getData(self):
        '''Returns the data in the node.'''
        return self._data

    def getNextLink(self):
        '''Returns the pointer to the next node.'''
        return self._nextLink

    def setData(self, newData):
        '''Insert data into node.'''
        self._data = newData

    def setNextLink(self, newNext):
        '''Set a pointer to next node/reference.'''
        self._nextLink = newNext


class UnorderedList:
    '''Implements an unorderedList with only a head pointer.'''

    def __init__(self):
        self._head = None
        self._size = 0

    def isEmpty(self):
        '''Checks if list is empty.Returns a boolean.'''
        return self._size == 0

    def add_front(self, item):
        '''adds a new item to the front of the list. O(1) operation'''
        temp = Node(item)
        temp.setNextLink(self._head)
        self._head = temp
        self._size += 1

    def pop_front(self):
        '''Remove front item and return its value.'''
        if self._head is None:
            raise IndexError('Out of bounds')
        current = self._head
        nxt = current.getNextLink()
        self._head = nxt
        self._size -= 1
        return current.getData()

    def size(self):
        '''returns the number of items in the list.'''
        return self._size

    def _find(self, item=None, idx=None):
        '''Find a node in a list.
           Arg:
             -item: Integer/Character/String/Object
           Returns:
             A tuple of the index and the current node and previous node
        '''
        current = self._head
        node = None
        pos = 0
        while pos < self._size:
            if current.getData() == item or pos == idx:
                node = current
                return pos, node
            else:
                current = current.getNextLink()
                pos += 1
        return None, None

    def search(self, item):
        '''Search for the item in the list.
           Arg:
            -item: Integer/String/Character/Object
           Returns
            A boolean.
        '''
        index, node = self._find(item)
        if node:
            return True
        return False

    def value_at(self, index):
        '''Returns the value of the nth item at given index.'''
        index, node = self._find(idx=index)
        if node:
            return node.getData()
        else:
            raise IndexError('Out of bounds')

    def remove(self, item):
        '''removes the item from the list. It needs the item and modifies
        the list. Returns None if item not in list.'''

        current = self._head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNextLink()
                # item to remove not in List.
                if current is None:
                    raise IndexError('Out of bounds')

        # item to be removed is first/head and connected to the head
        if previous is None:
            self._head = current.getNextLink()
        # item removal is anywhere in the list but not the head
        else:
            previous.setNextLink(current.getNextLink())

        self._size -= 1

    def append(self, item):
        '''adds a new item to the end of the list.'''
        temp = Node(item)
        current = self._head
        end = False
        while current is not None and not end:
            if current.getNextLink() is None:
                current.setNextLink(temp)
                end = True
            else:
                current = current.getNextLink()
        if current is None:
            self._head = temp

        self._size += 1

    def insert(self, pos, value):
        '''insert value at index, so current item at that index
           is pointed to by new item at index.
           Raise IndexError if index is out of range
        '''
        current = self._head
        index = 0
        found = False
        # insert outside the length limits of list.
        if pos > self._size - 1 or self._size == 0:
            raise IndexError('Out of bounds')
        while not found:
            if index == pos:
                found = True
            else:
                current = current.getNextLink()
                index += 1

        current.setData(value)

    def __setitem__(self, index, item):
        self.insert(index, item)

    def index(self, item):
        '''returns the position of item in the list.
           Raises index error if item not in the list.
        '''
        index, node = self._find(item)
        if node:
            return index
        else:
            raise IndexError('Out of bounds')

    def pop(self, index=None):
        '''removes and returns the last item in the list. It needs nothing
        and returns an item'''
        current = self._head
        previous = None
        end = False
        count = 0
        value = None
        # List is empty.
        if current is None:
            raise IndexError('Out of bounds')

        if index is not None:
            while current is not None and not end:
                if count == index:
                    end = True
                else:
                    previous = current
                    current = current.getNextLink()
                    count += 1
        else:
            while current is not None and not end:
                if current.getNextLink() is None:
                    end = True
                else:
                    previous = current
                    current = current.getNextLink()

        # list contains only one item which is at the head
        if previous is None:
            self._head = None
            value = current.getData()
        # List has more than one item.
        else:
            if current.getNextLink() is None:
                previous.setNextLink(None)
                value = current.getData()
            else:
                previous.setNextLink(current.getNextLink())
                value = current.getData()
        self._size -= 1
        return value

    def __getitem__(self, index):
        '''Returns the value of the indexed item.'''
        return self.value_at(index)

    def __len__(self):
        return self.size()

    def __iter__(self):
        current = self._head
        if current:
            while current is not None:
                yield current.getData()
                current = current.getNextLink()

    def front(self):
        '''Get value of front item.'''
        if self._head:
            return self._head.getData()
        else:
            raise IndexError('Out of bounds')

    def back(self):
        '''Get value at the end of list.'''
        current = self._head
        end = False
        if current is None:
            raise IndexError('Out of bounds')
        nxt = current.getNextLink()
        while not end:
            if nxt is None:
                end = True
            else:
                current = nxt
                nxt = current.getNextLink()
        if end:
            return current.getData()

    def reverse(self):
        '''Reverses the list.'''
        previous = None
        current = self._head
        end = False
        if current is None:
            raise IndexError('Out of bounds')
        nxt = current.getNextLink()
        while not end:
            current.setNextLink(previous)
            previous = current
            current = nxt
            if nxt:
                nxt = nxt.getNextLink()
            else:
                end = True
        self._head = previous


class UnorderedListTail(UnorderedList):
    '''Implements an unordered list with both the head and tail.'''

    def __init__(self):
        super().__init__()
        self._tail = None

    def add_front(self, item):
        '''adds a new item to the list. It needs the item and returns nothing.
        Assume the item is not already in the list.'''

        temp = Node(item)
        # Adding the first item to the list.
        if self._head is None:
            self._tail = temp
            self._head = temp
        else:
            temp.setNextLink(self._head)
            self._head = temp
        self._size += 1

    def append(self, item):
        '''adds a new item to the end of the list making it the last item in
        the collection.It needs the item and returns nothing. Assume the
        item is not already in the list. '''
        temp = Node(item)
        if self._head is None:
            self._head = temp
            self._tail = temp
        else:
            current = self._tail
            current.setNextLink(temp)
            self._tail = temp
        self._size += 1

    def pop(self, index=None):
        '''removes and returns the last item in the list. It needs nothing
        and returns an item'''
        current = self._head
        previous = None
        end = False
        count = 0
        value = None
        # List is empty.
        if current is None:
            raise IndexError('Out of bounds')

        if index is not None:
            while current is not None and not end:
                if count == index:
                    end = True
                else:
                    previous = current
                    current = current.getNextLink()
                    count += 1
        else:
            while not end:
                if current.getNextLink() is None:
                    end = True
                else:
                    previous = current
                    current = current.getNextLink()

        # list contains only one item which is at the head
        if previous is None:
            self._head = None
            value = current.getData()
        # List has more than one item.
        else:
            if current.getNextLink() is None:
                previous.setNextLink(None)
                self._tail = current
                value = current.getData()
            else:
                previous.setNextLink(current.getNextLink())
                value = current.getData()
        self._size -= 1
        return value

    def back(self):
        tail = self._tail
        if tail:
            return tail.getData()
        else:
            raise IndexError('Out of bounds')

    def reverse(self):
        '''Reverses the list.'''
        previous = None
        current = self._head
        end = False
        if current is None:
            raise IndexError('Out of bounds')
        nxt = current.getNextLink()
        self._tail = current
        while not end:
            current.setNextLink(previous)
            previous = current
            current = nxt
            if nxt:
                nxt = nxt.getNextLink()
            else:
                end = True
        self._head = previous


class OrderedList(UnorderedList):
    '''Implements an ordered list.'''

    def __init__(self):
        super().__init__()

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNextLink()

        return found

    def add_front(self, item):
        temp = Node(item)
        if self._head is None:
            self._head = temp
        else:
            current = self._head
            previous = None
            found = False
            while current is not None and not found:
                # item is placed at the head of the list
                if current.getData() > item and previous is None:
                    self._head = temp
                    temp.setNextLink(current)
                    found = True
                # item place in between the list
                elif current.getData() > item and previous.getData() < item:
                    temp.setNextLink(current)
                    previous.setNextLink(temp)
                    found = True
                else:
                    previous = current
                    current = current.getNextLink()

        self._size += 1

    def remove(self, item):
        '''removes the item from the list. It needs the item and modifies
        the list. Returns None if item not in list.'''

        current = self._head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNextLink()

        # item to remove not in List.
        if current is None:
            raise IndexError('Out of bounds')

        # item to be removed is first/head and connected to the head
        if previous is None:
            self._head = current.getNextLink()
        # item removal is anywhere in the list but not the head
        else:
            previous.setNextLink(current.getNextLink())

        self._size -= 1
# TODO: fix ordered linkedlist class
