'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import math


class Node:

    def __init__(self, value=None, next=None):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.next = next
        self.skip = None
        self.tf = 1
        self.score = 0.0


class LinkedList:
    """ Class to define a linked list (postings list). Each element in the linked list is of the type 'Node'
        Each term in the inverted index has an associated linked list object.
        Feel free to add additional functions to this class."""
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.length, self.n_skips, self.idf = 0, 0, 0.0
        self.skip_length = None

    def traverse_list(self):
        traversal = []
        if self.start_node is None:
            return
        else:
            """ Write logic to traverse the linked list.
                To be implemented."""
            for i in range(self.length):
                traversal.append(self.start_node.value)
                self.start_node = self.start_node.next
            return traversal
            raise NotImplementedError

    def traverse_skips(self):
        traversal = []
        if self.start_node is None:
            return
        else:
            """ Write logic to traverse the linked list using skip pointers.
                To be implemented."""
            for i in range(self.n_skips):
                traversal.append(self.start_node.value)
                self.start_node = self.start_node.skip
            return traversal
            raise NotImplementedError

    def add_skip_connections(self):
        n_skips = math.floor(math.sqrt(self.length))
        if n_skips * n_skips == self.length:
            n_skips = n_skips - 1
        """ Write logic to add skip pointers to the linked list. 
            This function does not return anything.
            To be implemented."""
        if self.length < 2:
            return
        self.n_skips = n_skips
        self.skip_length = math.floor(self.length / n_skips)
        node = self.start_node
        skip_node = None
        for i in range(n_skips):
            skip_node = node
            for j in range(self.skip_length):
                node = node.next
            skip_node.skip = node
        return
        raise NotImplementedError

    def insert_at_end(self, value):
        """ Write logic to add new elements to the linked list.
            Insert the element at an appropriate position, such that elements to the left are lower than the inserted
            element, and elements to the right are greater than the inserted element.
            To be implemented. """
        new_node = Node(value)
        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node
            self.length += 1
            return
        else:
            self.end_node.next = new_node
            self.end_node = new_node
            self.length += 1
            return
        raise NotImplementedError
    
    def calculate_tf_idf(self):
        """ Write logic to calculate tf-idf score for each document.
            To be implemented."""
        node = self.start_node
        while node is not None:
            node.score = node.tf * self.idf
            node = node.next
        return
        raise NotImplementedError
