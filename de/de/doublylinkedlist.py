"""A doubly linked list implementation."""

# DONE: Implement the following methods:
# __init__ - Initialize the a ListNode.
# __init__ - Initialize the doubly linked list.
# __len__ - Return the length of the list.
# addfirst - Add a node with the provided item to the front of the list.
# addlast - Add a node with the provided item to the end of the list.
# removefirst - Remove the first node from the list and return its item.
# removelast - Remove the last node from the list and return its item.
# __add__ - Concatenate the other list to the end of this list and return the new list (i.e., +)
# __iadd__ - Concatenate the other list to the end of this list and update the current list (i.e., +=).

from copy import deepcopy


class ListNode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def _addbetween(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def addfirst(self, item):
        self._addbetween(item, None, self._head)

    def addlast(self, item):
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        before, after = node.prev, node.link
        if node is self._head:
            self._head = after
        else:
            before.link = after
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def removefirst(self):
        return self._remove(self._head)

    def removelast(self):
        return self._remove(self._tail)

    def display(self):
        current = self._head
        while current is not None:
            print(current.data)
            current = current.link

    def __add__(self, other):
        self_copied = deepcopy(self)
        self_copied += other
        return self_copied

    def __iadd__(self, other):
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                self._tail.link = other._head
                other._head.prev = self._tail
            self._tail = other._tail
            self._length = self._length + other._length
            other.__init__()
        return self
