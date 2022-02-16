"""
Basic class definitions for a Linked List
"""


################################################################################
# Linked List
class LinkedList:
    def __init__(self):
        self.head = None


################################################################################
# Node in the Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


################################################################################
