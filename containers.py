class Container:
    """ The super class Container """

    def __init__(self):
        """ Constructor that creates a python
        list for each object of the class """

        self.items = []

    def size(self):
        """ Method that returns the number of elements
        in the objects list """

        return len(self.items)

    def is_empty(self):
        """ Method that check if the object´s list is empty """

        if not self.items:
            return True

        return False

    def push(self, item):
        """ Method that adds an item to the end of object´s
        list of items """

        self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass


class Queue(Container):
    """ Class for the container-type: Queue
     First in --> First out, FIFO """

    def __init__(self):
        super().__init__()

    def pop(self):
        """ Method that deletes and returns the first element // FIFO """
        assert not self.is_empty()  # Raising error if list is empty
        return self.items.pop(0)

    def peek(self):
        """ Method that returns the first element in the queue without deleting it """
        assert not self.is_empty()  # Raising error if list is empty
        return self.items[0]


class Stack(Container):
    """ Class for the container-type: Stack
    Last in --> First out, LIFO """

    def __init__(self):
        super().__init__()

    def pop(self):
        """ Method that deletes and returns the last element // LIFO """
        assert not self.is_empty()  # Raising error if list is empty
        return self.items.pop()

    def peek(self):
        """ Method that returns the top element of the stack without deleting it """
        assert not self.is_empty()  # Raising error if list is empty
        return self.items[len(self.items) - 1]
