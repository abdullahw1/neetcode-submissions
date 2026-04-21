class Node:
  def __init__(self, value, next=None, prev=None):
    self.value = value
    self.next = next
    self.prev = prev
class Deque:
  def __init__(self):
    # This method is the constructor for the Deque class.
    # It's called automatically when you create a new Deque object, like:
    # my_deque = Deque()

    # Initialize the internal data structure for the deque.
    # We're using a doubly linked list with dummy head and tail nodes
    # to make adding and removing elements from both ends efficient (O(1)).

    # Create a dummy head node. This node will always be the first node
    # in our internal linked list. It does NOT store any actual data from
    # the deque. We give it a value of 0 (or any arbitrary value, as it won't
    # be accessed as deque data).
    self.head = Node(0)

    # Create a dummy tail node. This node will always be the last node
    # in our internal linked list. It also does NOT store any actual data.
    # We give it a value of 0 for consistency, though the value is irrelevant.
    self.tail = Node(0)

    # Initially, the deque is empty.
    # We link the dummy head's 'next' pointer to the dummy tail node.
    # This means that from the dummy head, the very next node is the dummy tail.
    # This is how we represent an empty list: there are no actual data nodes
    # between the head and the tail.
    self.head.next = self.tail

    # Similarly, we link the dummy tail's 'prev' pointer back to the dummy head node.
    # This completes the link for an empty list, where the dummy tail's previous
    # node is the dummy head.
    self.tail.prev = self.head


  def isEmpty(self) -> bool:
    # Deque is empty if dummy head's next pointer points to the dummy tail.
    # In an empty list, there are no actual nodes between the dummy head and tail.
    return self.head.next == self.tail
  
  def append(self, value: int) -> None:
    new_node = Node(value)              # Create a new node to hold the value.
    last_node = self.tail.prev          # Get the node currently before the dummy tail (the last element).
    last_node.next = new_node           # Link the previous last node's 'next' to the new node.

    new_node.prev = last_node           # Link the new node's 'prev' back to the previous last node.
    new_node.next = self.tail           # Link the new node's 'next' to the dummy tail.
    self.tail.prev = new_node           # Update the dummy tail's 'prev' to point to the new node.
    # Note: A size counter should also be incremented here.

  def appendleft(self, value: int) -> None:
    new_node = Node(value)              # Create a new node to hold the value.
    first_node = self.head.next         # Get the node currently after the dummy head (the first element).
    self.head.next = new_node           # Link the dummy head's 'next' to the new node.
    new_node.prev = self.head           # Link the new node's 'prev' back to the dummy head.
    new_node.next = first_node          # Link the new node's 'next' to the previous first node.
    first_node.prev = new_node          # Update the previous first node's 'prev' to point to the new node.
    # Note: A size counter should also be incremented here.

  def pop(self) -> int:
    if self.isEmpty():                  # Check if the deque is empty.
      return -1                         # If empty, return -1 as specified.
    target_node = self.tail.prev        # Get the last node (node before the dummy tail). This is the one to remove.
    value = target_node.value           # Store the value of the node we are about to remove.
    prev_node = target_node.prev        # Get the node before the target node.
    prev_node.next = self.tail          # Link the previous node's 'next' to the dummy tail, effectively skipping the target node.
    self.tail.prev = prev_node          # Update the dummy tail's 'prev' to point to the node before the one just removed.
    # Optional: target_node.next = None # Disconnect the removed node for garbage collection (not shown in your code but good practice)
    # Optional: target_node.prev = None # Disconnect the removed node for garbage collection (not shown in your code but good practice)
    # Note: A size counter should also be decremented here.
    return value                        # Return the stored value of the removed node.

  def popleft(self) -> int:
    if self.isEmpty():                  # Check if the deque is empty.
      return -1                         # If empty, return -1.
    target_node = self.head.next        # Get the first node (node after the dummy head) to remove.
    value = target_node.value           # Store the value of the node being removed.
    next_node = target_node.next        # Get the node that comes after the target node.
    self.head.next = next_node          # Link the dummy head's 'next' to the node after the target, skipping the target.
    next_node.prev = self.head          # Link the next node's 'prev' back to the dummy head.
    # Optional: target_node.next = None # Disconnect the removed node.
    # Optional: target_node.prev = None # Disconnect the removed node.
    # Note: Decrement size counter here.
    return value                        # Return the stored value.