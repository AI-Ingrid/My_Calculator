import re
import numbers as num
import numpy as np
from function import Function
from operator_class import Operator
from containers import Queue, Stack


class Calculator:
    """ Calculator class"""
    def __init__(self):
        self.functions = {
            'EXP': Function(np.exp),
            'LOG': Function(np.log),
            'SIN': Function(np.sinc),
            'COS': Function(np.cos),
            'SQRT': Function(np.sqrt)
        }
        self.operators = {
            'ADD': Operator(np.add, 0),
            'PLUS': Operator(np.add, 0),
            'MULTIPLY': Operator(np.multiply, 1),
            'TIMES': Operator(np.multiply, 1),
            'DIVIDE': Operator(np.divide, 1),
            'SUBTRACT': Operator(np.subtract, 0),
            'MINUS': Operator(np.subtract, 0)
        }
        self.output_queue = Queue()

    def rpn(self):
        """ Method that writes calculation is a reverse-polish-notation """
        temp_stack = Stack()
        temp_result = 0

        while self.output_queue.items:
            item = self.output_queue.pop()

            # Case 1: Item is a number
            if isinstance(item, num.Number):
                temp_stack.push(item)

            # Case 2: Item is a function
            elif isinstance(item, Function):
                temp_num = temp_stack.pop()
                temp_result = item.execute(temp_num)
                temp_stack.push(temp_result)

            # Case 3: Item is an operator
            elif isinstance(item, Operator):
                last_num = temp_stack.pop()
                next_last_num = temp_stack.pop()
                temp_result = item.execute(next_last_num, last_num)
                temp_stack.push(temp_result)
            print("Temp stack: " + str(temp_stack.items))

        print("-----------------------------------------------")
        print("This is the solution: " + str(temp_stack.peek()))
        return temp_stack.peek()

    def shunting_yard(self, input_queue):
        """ Method that builds a RPN queue """
        temp_operator_stack = Stack()

        while not input_queue.is_empty():
            element = input_queue.pop()

            # Case 1:
            if isinstance(element, num.Number):
                self.output_queue.push(element)

            # Case 2:
            elif isinstance(element, Function):
                temp_operator_stack.push(element)

            # Case 3:
            elif element == '(':
                temp_operator_stack.push(element)

            # Case 4:
            elif element == ')':

                while not temp_operator_stack.is_empty():
                    temp_element = temp_operator_stack.peek()

                    if temp_element == '(':
                        break

                    temp_operator_stack.pop()
                    self.output_queue.push(temp_element)

                top_stack_element = temp_operator_stack.peek()

                if top_stack_element == '(':
                    temp_operator_stack.pop()

                elif isinstance(top_stack_element, Function):
                    temp_element = temp_operator_stack.pop()
                    self.output_queue.push(temp_element)

            # Case 5:
            elif isinstance(element, Operator):

                while not temp_operator_stack.is_empty():
                    temp_top_element = temp_operator_stack.peek()

                    if isinstance(temp_top_element, Operator):
                        if element.strength >= temp_top_element.strength:
                            break
                        else:
                            temp_operator_stack.pop()

                    elif temp_top_element == '(':
                        break

                    self.output_queue.push(temp_top_element)

                temp_operator_stack.push(element)

        while not temp_operator_stack.is_empty():
            temp_item = temp_operator_stack.pop()
            self.output_queue.push(temp_item)

        print("The final output queue: " + str(self.output_queue.items))

        return self.output_queue

    def text_parsing(self, text_string):
        """ Method that recognizes the different parts of the input
        text and produces the element list for shunting yard """

        # Creating a Queue to push elements to in order to create a queue for shunting yard
        output_queue = Queue()
        text_string = text_string.replace(" ", "").upper()

        # Parsing
        function_targets = "|".join(["^" + function for function in self.functions.keys()])
        operator_targets = "|".join(["^" + operator for operator in self.operators.keys()])

        current_index = 0

        while len(text_string) != 0:
            #print("Text string: " + text_string)

            # Searching for matches
            function_match = re.search(function_targets, text_string)
            operator_match = re.search(operator_targets, text_string)
            number_match = re.search("^[-0123456789.]+", text_string)
            symbol_match = re.search("^[()]", text_string)

            # Finding functions matches
            if function_match is not None:
                function = function_match.group(0)
                print("Function match found: " + str(function))
                output_queue.push(self.functions[function])
                current_index = function_match.end()

            # Finding operator matches
            elif operator_match is not None:
                operator = operator_match.group(0)
                print("Operator match found: " + str(operator))
                output_queue.push(self.operators[operator])
                current_index = operator_match.end()

            # Finding number matches
            elif number_match is not None:
                number = number_match.group(0)
                print("Number match found: " + str(number))
                output_queue.push(float(number))
                current_index = number_match.end()

            # Finding parentheses matches
            elif symbol_match is not None:
                symbol = symbol_match.group(0)
                print("Parenthese match found: " + str(symbol))
                output_queue.push(symbol)
                current_index = symbol_match.end()

            # "Deleting" the  parsed string
            text_string = text_string[current_index:]

        print(str(output_queue.items))
        return output_queue
