#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())
    
    def __iter__(self):
        return self

    def __next__(self):
        current = self.head

        while current.next is not None:
            yield current
            current = current.next

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) which is linear complexity, as the list increases, the time taken for the algorithm to complete also increases at exactly the same rate as the input """
        # TODO: Loop through all nodes and count one for each
        count = 0
        for node in self.items():
            count += 1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: 0(1) which is constant complexity because it only has to check and change the tail end"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
        elif self.head.next is None:
            self.head.next = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) which is constant complexity because it only needs to check the head and replace it"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)

        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) if item is the self.head
        TODO: Worst case running time: O(n) runs through n loops once"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        node = self.head

        while node is not None:
            if quality(node.data):
                return node.data
            else:
                node = node.next
        return None
    
    def replace(self, item, new):
        """Replace item with new item"""

        node = self.head

        while node is not None:
            if node.data == item:
                node.data = new
                return
            else:
                node = node.next
            
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) if item is the self.head
        TODO: Worst case running time: O(n) runs through n loops once"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        current = self.head
        previous = None

        while current is not None:
            if item == current.data:
                # OFF WITH THE HEAD
                if previous is None:
                    self.head = current.next
                    # HEAD BUTT
                    if current.next is None:
                        self.tail = previous
                # JUNK THE TRUNK
                elif current.next is None:
                    previous.next = None
                    self.tail = previous
                # THE NEUROTYPICALS
                else:
                    previous.next = current.next
                return None
            # ADVANCING THE GAY AGENDA
            else:
                previous = current
                current = current.next

        raise ValueError('Item not found: {}'.format(item)) 


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    print('\nTesting prepend:')
    for item in ['1', '2', '3']:
        print('prepend({!r})'.format(item))
        ll.prepend(item)
        print('list: {}'.format(ll))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
