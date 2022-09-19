import numbers


class Function:
    """ Super class for the calculator´s different functions """
    def __init__(self, function):
        self.function = function

    def execute(self, element, debug=True):
        """ Method that checks type """
        if not isinstance(element, numbers.Number):
            raise TypeError("The element must be a number")  # Raising error element is not a number

        result = self.function(element)  # Parameter in variable because of np-input in init

        # Report
        if debug is True:
            print("Function: " + self.function.__name__ + "({:f}) = {:f}".format(element, result))

        return result
