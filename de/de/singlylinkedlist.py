"""A singly linked list implementation."""

# DONE: Implement the following methods:
# __init__ - Initialize the a ListNode.
# __init__ - Initialize the singly linked list.
# __len__ - Return the length of the list.
# addfirst - Add a node with the provided item to the front of the list.
# addlast - Add a node with the provided item to the end of the list.
# removefirst - Remove the first node from the list and return its item.
# removelast - Remove the last node from the list and return its item.
# __add__ - Concatenate the other list to the end of this list and return the new list (i.e., +)
# __iadd__ - Concatenate the other list to the end of this list and update the current list (i.e., +=).

from copy import deepcopy


class ListNode:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def addlast(self, item):
        if self._head is None:
            self.addfirst(item)
        else:
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
            self._length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        if self._head is self._tail:
            return self.removefirst()
        else:
            currentnode = self._head
            while currentnode.link is not self._tail:
                currentnode = currentnode.link
            item = self._tail.data
            self._tail = currentnode
            self._tail.link = None
            self._length -= 1
            return item

    def __len__(self):
        return self._length

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
            self._tail = other._tail
            self._length = self._length + other._length
            other.__init__()
        return self
