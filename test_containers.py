import unittest
from containers import Queue, Stack

items = [1, 2, 3, 4, 5, 6, 7, 8]
zero_items = []


class TestContainer(unittest.TestCase):

    def test_size(self):
        print('.. Testing the "test_size" method ..')
        self.assertEqual(len(items), 8, "Should be 8")

    def test_is_empty(self):
        print('.. Testing the "is_empty" method ..')
        # The truth
        items_is_empty = False
        zero_items_is_empty = True

        # Declaring the state variables
        result_items_is_empty = False
        result_zero_items_is_empty = False

        if not items:
            result_items_is_empty = True

        if not zero_items:
            result_zero_items_is_empty = True

        # Checking an NOT empty list
        self.assertEqual(result_items_is_empty, items_is_empty, "They should be equal. Both empty")

        # Checking a empty list
        self.assertEqual(result_zero_items_is_empty, zero_items_is_empty, "They should be equal")

    def test_push(self):
        print(".. Testing the push method ..")
        test_items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        test_items_2 = [1, 2, 3, 4, 5, 6, 7, 8]

        test_items_2.append(9)
        self.assertEqual(test_items_2[8], test_items[8], "they should be 9")


class TestQueue(unittest.TestCase):

    def test_pop(self):
        # Creating a Queue object
        test_queue = Queue()
        # Pushing elements to the Queue object
        test_queue.push(1)
        test_queue.push(2)
        test_queue.push(3)
        test_queue.push(4)

        while not test_queue.is_empty():
            print("This is the queue: " + str(test_queue.items))
            print("Removing: " + str(test_queue.pop()) + " from the queue")
            print("Items left in the queue: " + str(test_queue.size()))


class TestStack(unittest.TestCase):

    def test_pop(self):
        test_stack = Stack()
        test_stack.items.push(6)
        test_stack.items.push(8)
        test_stack.items.push(3)
        test_stack.items.push(10)

        while not test_stack.is_empty():
            print("This is the stack: " + str(test_stack.items))
            print("Removing: " + str(test_stack.pop()) + " from the stack")
            print("Items left in the stack: " + str(test_stack.size()))


if __name__ == "__main__":
    unittest.main()

