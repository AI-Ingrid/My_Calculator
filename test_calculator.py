from calculator import Calculator
from containers import Queue


def main_4_and_5():
    calc = Calculator()

    # Test for the 4th implementation
    print(" --> This is a test for the 4th implementation")
    print(calc.functions['EXP'].execute(              # Creating a Function object that has funtion np.exp then calls the exp(element) -- meaning e^something
        calc.operators['ADD'].execute(1,              # Creating a Operator object that has np.ass as operator then calls the add(1, something)
        calc.operators['MULTIPLY'].execute(2, 3))))   # Creating a Operator object that has np.multiply as operator then calls multiply(2,3)

    # Test for the 5th implementation
    print("--> This is a test for the 5th implementation")
    calc_2 = Calculator()

    # Building a output queue for testing
    calc_2.output_queue.push(1)
    calc_2.output_queue.push(2)
    calc_2.output_queue.push(3)
    calc_2.output_queue.push(calc_2.operators["MULTIPLY"])
    calc_2.output_queue.push(calc_2.operators["ADD"])
    calc_2.output_queue.push(calc_2.functions["EXP"])

    calc_2.rpn()


def main_6_part_1():
    calc = Calculator()
    input_queue = Queue()

    # Building a input queue for testing
    input_queue.push(calc.functions['EXP'])
    input_queue.push('(')
    input_queue.push(1)
    input_queue.push(calc.operators['ADD'])
    input_queue.push(2)
    input_queue.push(calc.operators['MULTIPLY'])
    input_queue.push(3)
    input_queue.push(')')

    calc.shunting_yard(input_queue)


def main_6_part_2():
    calc = Calculator()
    input_queue = Queue()

    # Building a input queue for testing
    input_queue.push(2)
    input_queue.push(calc.operators['MULTIPLY'])
    input_queue.push(3)
    input_queue.push(calc.operators['ADD'])
    input_queue.push(1)

    calc.shunting_yard(input_queue)


def main_8_1():
    calc_1 = Calculator()

    # Input strings
    input_string_1 = "exp(1 add 2 multiply 3)"

    # Creating text queues with text parsing
    print("-------------------------------------- text parsing ---------------------------")
    text_queue_1 = calc_1.text_parsing(input_string_1)

    # Updating the self.output_queue in calc in order to use rpn algorithm
    print("--------------------------------------Shunting yard----------------------------")
    calc_1.shunting_yard(text_queue_1)

    # Uses rpn on self.output_queue in order to perform the calculation
    print("--------------------------------------RPN--------------------------------------")
    calc_1.rpn()


def main_8_2():
    calc_2 = Calculator()

    # Input strings
    input_string_2 = "((15 divide (7 subtract (1 add 1))) multiply 3) subtract (2 add (1 add 1))"

    # Creating text queues with text parsing
    print("-------------------------------------- text parsing ---------------------------")
    text_queue_2 = calc_2.text_parsing(input_string_2)

    # Updating the self.output_queue in calc in order to use rpn algorithm
    print("--------------------------------------Shunting yard----------------------------")
    calc_2.shunting_yard(text_queue_2)

    # Uses rpn on self.output_queue in order to perform the calculation
    print("--------------------------------------RPN--------------------------------------")
    calc_2.rpn()

#main_4_and_5()
#main_6_part_1()
#main_6_part_2()
#main_8_1()
main_8_2()
