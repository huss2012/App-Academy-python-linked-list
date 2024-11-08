"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here
class Node:
  # TODO: Set the `_value` `_next` node instance variables
  def __init__(self, value):
    self._value = value
    self._next = None


# TODO: Implement a Singly Linked List class here
class LinkedList:
  # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
  def __init__(self):
    self._head = None
    self._tail = None
    self._length = 0

  # TODO: Implement the get_node method here
  def get_node(self, position):
    if position < 0 or position >= self._length:
      return

    current_node = self._head
    current_position = 0

    while current_position < position:
      current_node = current_node._next

      current_position += 1

    return current_node

  # TODO: Implement the add_to_tail method here
  def add_to_tail(self, value):
    new_node = Node(value)

    if self._length == 0:
      self._head = new_node
      self._tail = new_node

    else:
      self._tail._next = new_node
      self._tail = new_node

    self._length += 1

  # TODO: Implement the add_to_head method here
  def add_to_head(self, value):
    new_node = Node(value)

    #If the list is empty
    if self._length == 0:
      self._head = new_node
      self._tail = new_node
    else:
      new_node._next = self._head
      self._head = new_node
    self._length += 1

  # TODO: Implement the remove_head method here
  def remove_head(self):
    if self._length == 0:
      return None

    removed_value = self._head._value

    self._head = self._head._next

    if self._head is None:
      self._tail = None

    self._length -= 1

    return removed_value

  # TODO: Implement the remove_tail method here
  def remove_tail(self):
    if self._length == 0:
      return None

    removed_value = self._tail._value

    if self._length == 1:
      self._head = None
      self._tail = None
    else:
      current_node = self._head

      while current_node._next is not self._tail:
        current_node = current_node._next

      self._tail = current_node
      self._tail.new = None

      self._length -= 1

      return removed_value

  # TODO: Implement the __len__ method here
  def __len__(self):
    return self._length

# Phase 2

  # TODO: Implement the contains_value method here
  def contains_value(self, target):
    current_node = self._head

    while current_node is not None:
      if current_node._value == target:
        return True
      current_node = current_node._next
    return False

  # TODO: Implement the insert_value method here
  def insert_value(self, position, value):
    if position < 0 or position > self._length:
          raise IndexError("Position out of bounds")

    new_node = Node(value)

    if position == 0:
        # Insert at the head
        new_node._next = self._head
        self._head = new_node
        if self._length == 0:
            # If the list was empty, set the tail as well
            self._tail = new_node
    elif position == self._length:
        # Insert at the tail
        self._tail._next = new_node
        self._tail = new_node
    else:
        # Insert at the middle
        prev_node = self.get_node(position - 1)
        new_node._next = prev_node._next
        prev_node._next = new_node

      # Increment the length of the list
    self._length += 1

  # TODO: Implement the update_value method here
  def update_value(self, position, value):

    if position < 0 or position >= self._length:
        raise IndexError("Position out of bounds")

    # Get the node at the specified position
    node_to_update = self.get_node(position)
    # Update the node's value
    node_to_update._value = value

  # TODO: Implement the remove_node method here
  def remove_node(self, position):
    if position < 0 or position >= self._length:
            raise IndexError("Position out of bounds")

    # Special case: remove the head node
    if position == 0:
        return self.remove_head()

    # Special case: remove the tail node
    if position == self._length - 1:
        return self.remove_tail()

    # General case: remove node in the middle
    previous_node = self.get_node(position - 1)
    node_to_remove = previous_node._next

    # Bypass the node to remove
    previous_node._next = node_to_remove._next

    # Decrease the length of the list
    self._length -= 1

    return node_to_remove._value

  # TODO: Implement the __str__ method here
  def __str__(self):
    if self._head is None:
          return "Empty List"

    # Initialize an empty list to accumulate values as strings
    values = []
    current_node = self._head

    # Traverse the linked list and append each node's value
    while current_node:
        values.append(str(current_node._value))
        current_node = current_node._next

    # Join the values with " -> " as a separator to represent the linked list structure
    values_string = " -> ".join(values)

    return values_string

# Phase 1 Manual Testing:

# 1. Test Node and LinkedList initialization
node = Node('hello')
print(node)                                     # <__main__.Node object at ...>
print(node._value)                              # hello
linked_list = LinkedList()
print(linked_list)                              # <__main__.LinkedList object at ...>

# # 2. Test getting a node by its position
print(linked_list.get_node(0))                # None

# # 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0)._value)         # `new tail node`

# # 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
print(linked_list.get_node(0))                # <__main__.Node object at ...>
print(linked_list.get_node(0)._value)         # `new head node`

# # 5. Test removing the head node
linked_list.remove_head()
print(linked_list.get_node(0)._value)         # `new tail node` because `new head node` has been removed
print(linked_list.get_node(1))                # `None` because `new head node` has been removed

# # 6. Test removing the tail node
print(linked_list.get_node(0)._value)         # `new tail node`
linked_list.remove_tail()
print(linked_list.get_node(0))                # None

# # 7. Test returning the list length
print(len(linked_list))                                 # 2

# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
print(linked_list.contains_value('new head node'))      # True
print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
print(linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
linked_list.update_value(0, 'goodbye!')
print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
print(linked_list.get_node(1)._value)                   # `new head node`
linked_list.remove_node(1)
print(linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
new_linked_list = LinkedList()
print(new_linked_list)                  # Empty List
new_linked_list.add_to_tail('puppies')
print(new_linked_list)                  # puppies
new_linked_list.add_to_tail('kittens')
print(new_linked_list)                  # puppies, kittens
